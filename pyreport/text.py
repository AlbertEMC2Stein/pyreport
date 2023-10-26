from .base import LaTeXObject
from .utils import indented_write


class PlainText(LaTeXObject):
    """A class to hold plain text."""

    def __init__(self, text, name="plaintext"):
        """Constructor for PlainText.

        Parameters
        ----------
        text : str
            Text to hold.
        name : str, optional
            Name of object, by default "plaintext".
        """

        super().__init__("plaintext")
        self._text = text

    def texify(self, file, indent_level=0):
        tex = self._text.replace("\n", "\n\n")
        indented_write(file, indent_level, tex)