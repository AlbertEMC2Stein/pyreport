"""A module for generating LaTeX figures."""

import os

from .base import LaTeXObject
from .utils import indented_write


class Image(LaTeXObject):
    """ Class to hold images. """

    def __init__(self, image_file, name, width=1.0, caption="", label=""):
        """Constructor for Image.

        Parameters
        ----------
        image_file : str
            Path to image file.
        name : str
            Name of image.
        width : float, optional
            Width of image as fraction of linewidth, by default 1.0.
        caption : str, optional
            Caption of image, by default "".
        label : str, optional
            Label of image, by default "".
        """
        super().__init__(name)
        self._image_file = image_file
        self._width = width
        self._caption = caption
        self._label = label

    def texify(self, file, indent_level=0):
        # Copy image to out folder
        image_name = os.path.basename(self._image_file)
        image_file = os.path.join("out", "figures", image_name)
        os.makedirs(os.path.dirname(image_file), exist_ok=True)
        os.system(f"cp {self._image_file} {image_file}")
        tex = "\\begin{figure}[ht]\n"
        tex += "\t\\centering\n"
        tex += f"\t\\includegraphics[width={self._width}\\linewidth]{{{os.path.join('figures', image_name)}}}\n"
        tex += f"\t\\caption{{{self._caption}}}\n" if self._caption else ""
        tex += f"\t\\label{{fig:{self._label}}}\n" if self._label else ""
        tex += "\\end{figure}\n"


        indented_write(file, indent_level, tex)