from abc import ABC, abstractmethod


class Environment(ABC):
    """Abstract base class for all environments."""

    @abstractmethod
    def __init__(self, name):
        """Constructor for Environment. Note that this class cannot not be instantiated.
        
        Parameters
        ----------
        name : str
            Name of environment.
        """

        self._name = name
        self._contents = []

    @abstractmethod
    def texify(self, file, indent_level=0):
        """Writes the environment to a .tex-file.
        
        Parameters
        ----------
        file : file
            File to write to.
        indent_level : int, optional
            Indentation level, by default 0.
        """

    @abstractmethod
    def add_to_content(self, obj):
        """Adds an object to the environment.

        Parameters
        ----------
        obj : Environment, LaTeXObject
            Object to add to environment.
        """

        # FIXME: The following checks should be enforced in some other way.
        # We cannot import these classes here.
        # if isinstance(obj, Document):
        #     raise TypeError("Cannot add Document to Environment.")

        # if isinstance(obj, Preamble):
        #     raise TypeError("Cannot add Preamble to Environment.")

        self._contents.append(obj)

    @abstractmethod
    def get_structure(self, indent_level=0):
        """Returns the structure of the environment as a string.

        Parameters
        ----------
        indent_level : int, optional
            Indentation level, by default 0.
        """

        result = f"{self}\n"
        for i, content in enumerate(self._contents):
            glyph = "└──" if i == len(self._contents) - 1 else "├──"

            if isinstance(content, Environment):
                result += (
                    indent_level * "│    "
                    + f"{glyph} {content.get_structure(indent_level + 1)}"
                )

        return result

    @abstractmethod
    def __str__(self):
        return f"{self.__class__.__name__}: {self._name:<12}"

