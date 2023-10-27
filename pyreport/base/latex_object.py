from abc import ABC, abstractmethod


class LaTeXObject(ABC):
    """Abstract base class for all LaTeX objects."""

    def __init__(self, name):
        """Constructor for LaTeXObject. Note that this class cannot not be instantiated.

        Parameters
        ----------
        name : str
            Name of object.
        """

        self._name = name

    @abstractmethod
    def texify(self, file, indent_level=0):
        """Writes the object to a .tex-file.

        Parameters
        ----------
        file : file
            File to write to.
        indent_level : int, optional
            Indentation level, by default 0.
        """

    def __str__(self):
        return f"LaTeXObject: {self._name:<12}"
