from .base import Environment
from .utils import indented_write


_level_prefix_assignment = {
    "chapter": (0, "ch"),
    "section": (1, "sec"),
    "subsection": (2, "ssec"),
    "subsubsection": (3, "sssec"),
    "paragraph": (4, "par"),
}


class Segment(Environment):
    """A class to hold the LaTeX chapter, section, subsection, etc. environments."""

    def __init__(self, name, segment_type, label="", asterisk=False):
        """Constructor for Segment.

        Parameters
        ----------
        name : str
            Name of segment.
        segment_type : {"chapter", "section", "subsection", "subsubsection", "paragraph"}
            Type of segment.
        label : str, optional
            Label of segment, by default "".
        asterisk : bool, optional
            Whether to use asterisk, by default False.
        """

        super().__init__(name)
        self._label = label
        self._asterisk = asterisk
        self._segment_type = segment_type
        self._level = _level_prefix_assignment[segment_type][0]
        self._label_prefix = _level_prefix_assignment[segment_type][1]

    def texify(self, file, indent_level=0):
        asterisk = "*" if self._asterisk else ""

        create_command = f"\\{self._segment_type}{asterisk}{{{self._name}}}"
        indented_write(file, indent_level, create_command)

        if self._label:
            label_command = f"\\label{{{self._label_prefix}::{self._label}}}"
            indented_write(file, indent_level, label_command)

        for content in self._contents:
            content.texify(file, indent_level + 1)

        indented_write(
            file, indent_level, f"% End of {self._segment_type} '{self._name}'\n"
        )

    def add_to_content(self, obj):
        """Adds an object to the segment.
        
        Parameters
        ----------
        obj : Environment, LaTeXObject
            Object to add to segment.
        
        Raises
        ------
        TypeError
            Raised when Segment of lower level is tried to be added.
        """

        if isinstance(obj, Segment):
            levelo, levels = obj._level, self._level
            err_msg = f"Cannot add ChapterLike with lower level (self: {levels}, other: {levelo})."

            if levelo < levels:
                raise TypeError(err_msg)

        return super().add_to_content(obj)

    def get_structure(self, indent_level=0):
        # pylint: disable=useless-super-delegation
        return super().get_structure(indent_level)

    def __str__(self):
        return f"{self._segment_type.capitalize()}: {self._name}"
