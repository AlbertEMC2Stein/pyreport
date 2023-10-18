"""A module to create LaTeX reports.

This module provides a class to create LaTeX reports. It is based on the
LaTeX document classes 'article' and 'report'. The report is created in the
'out' folder and is compiled with 'latexmk'.
"""

import os
from abc import ABC, abstractmethod
from ._utils import restricted_get, indented_write

__all__ = ["ReportKwargs", "Reporter", "ReportError", "Environment", "Segment", "LaTeXObject", "make_test_report"]

###########################################################################################

class ReportKwargs:
    """A class to hold the arguments for the Reporter class."""

    def __init__(self, **kwargs):
        """Constructor for ReportKwargs.

        Parameters
        ----------
        type: {"article", "report"}, optional
            Type of report, by default "report".
        fontsize: {10, 11, 12}, optional
            Font size, by default 12.
        columns: {"onecolumn", "twocolumn"}, optional
            Number of columns, by default "onecolumn".
        titlepage: {"notitlepage", "titlepage"}, optional
            Title page, by default "notitlepage".
        packages: list, optional
            List of packages to import, by default [].
        author: str, optional
            Author of report, by default "".
        title: str, optional
            Title of report, by default "".
        date: str, optional
            Date of report, by default "\\today".
        maketitle: bool, optional
            Make title, by default True.
        maketoc: bool, optional
            Make table of contents, by default False.
        """

        self.type = restricted_get(kwargs, "type", ["article", "report"], "report")
        self.fontsize = restricted_get(kwargs, "fontsize", [10, 11, 12], 12)
        self.columns = restricted_get(
            kwargs, "columns", ["onecolumn", "twocolumn"], "onecolumn"
        )
        self.titlepage = restricted_get(
            kwargs, "titlepage", ["notitlepage", "titlepage"], "notitlepage"
        )
        self.packages = restricted_get(kwargs, "packages", list, [])
        self.author = restricted_get(kwargs, "author", str, "")
        self.title = restricted_get(kwargs, "title", str, "")
        self.date = restricted_get(kwargs, "date", str, "\\today")
        self.maketitle = restricted_get(kwargs, "maketitle", bool, True)
        self.maketoc = restricted_get(kwargs, "maketoc", bool, False)

    def to_dict(self):
        """Returns a dictionary with the arguments."""
        return {
            "type": self.type,
            "fontsize": self.fontsize,
            "columns": self.columns,
            "titlepage": self.titlepage,
            "packages": self.packages,
            "author": self.author,
            "title": self.title,
            "date": self.date,
            "maketitle": self.maketitle,
            "maketoc": self.maketoc,
        }


class Reporter:
    """A class to create LaTeX reports."""

    def __init__(self, report_name, report_kwargs):
        """Constructor for Reporter.
        
        Parameters
        ----------
        report_name : str
            Name of report.
        report_kwargs : ReportKwargs
            Arguments for report.
        """

        self._report_name = report_name
        self._report_contents = [
            Preamble(**report_kwargs.to_dict()),
            Document(**report_kwargs.to_dict()),
        ]

    def add_to_document(self, obj):
        """Adds an object to the document.

        Parameters
        ----------
        obj : Environment, LaTeXObject
            Object to add to document.
        """

        self._report_contents[1].add_to_content(obj)

    def report(self):
        """Creates and compiles the report.

        Raises
        ------
        ReportError
            Raised when report cannot be made.
        """

        try:
            print("Writing report...")
            if not os.path.exists("out"):
                os.mkdir("out")

            file_path = os.path.join("out", self._report_name + ".tex")
            with open(file_path, "w", encoding="utf8") as f:
                self._report_contents[0].texify(f)
                self._report_contents[1].texify(f)

            print("Done!\nCompiling report...")

            os.system(f"latexmk -cd -pdf -quiet {file_path}")
            os.system(f"latexmk -cd -c {file_path}")

            print("Done!")
        except Exception as e:
            raise ReportError("Report could not be made.") from e

    def print_structure(self):
        """Prints the structure of the report."""
        print("Report structure:")
        print(self._report_contents[1].get_structure())


class ReportError(Exception):
    """Raised when report cannot be made."""


###########################################################################################

_level_prefix_assignment = {
    "chapter": (0, "ch"),
    "section": (1, "sec"),
    "subsection": (2, "ssec"),
    "subsubsection": (3, "sssec"),
    "paragraph": (4, "par"),
}


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

        if isinstance(obj, Document):
            raise TypeError("Cannot add Document to Environment.")

        if isinstance(obj, Preamble):
            raise TypeError("Cannot add Preamble to Environment.")

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


class Document(Environment):
    """A class to hold the LaTeX document environment."""

    def __init__(self, name="document", **kwargs):
        """Constructor for Document.

        Parameters
        ----------
        name : str, optional
            Name of document, by default "document".
        **kwargs : dict
            Arguments for document.
        """

        super().__init__(name)
        self._type = kwargs["type"]
        self._titlepage = kwargs["titlepage"]
        self._title = kwargs["title"]
        self._author = kwargs["author"]
        self._date = kwargs["date"]
        self._maketitle = kwargs["maketitle"]
        self._maketoc = kwargs["maketoc"]

    def texify(self, file, indent_level=0):
        indented_write(file, indent_level, "\\begin{document}")

        if (self._title or self._author or self._date) and self._maketitle:
            indented_write(
                file, indent_level + 1, "\\maketitle\n" if self._maketitle else "", end=""
            )

        # small hack because those two options interfere with each other
        toc_command = r"\tableofcontents"
        if self._titlepage == "notitlepage" and self._type == "report":
            toc_command = r"{\let\clearpage\relax\tableofcontents}"

        indented_write(
            file, indent_level + 1, toc_command + "\n" if self._maketoc else ""
        )

        for content in self._contents:
            content.texify(file, indent_level + 1)

        indented_write(file, indent_level, "\\end{document}")

    def add_to_content(self, obj):
        # pylint: disable=useless-super-delegation
        super().add_to_content(obj)

    def get_structure(self, indent_level=0):
        # pylint: disable=useless-super-delegation
        return super().get_structure(indent_level)

    def __str__(self):
        # pylint: disable=useless-super-delegation
        return super().__str__()


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


###########################################################################################


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


class Preamble(LaTeXObject):
    """A class to hold the LaTeX preamble."""

    def __init__(self, name="preamble", **kwargs):
        """Constructor for Preamble.

        Parameters
        ----------
        name : str, optional
            Name of preamble, by default "preamble".
        **kwargs : dict
            Arguments for preamble.
        """

        super().__init__(name)
        self._type = kwargs["type"]
        self._fontsize = kwargs["fontsize"]
        self._columns = kwargs["columns"]
        self._titlepage = kwargs["titlepage"]
        self._packages = kwargs["packages"]
        self._author = kwargs["author"]
        self._title = kwargs["title"]
        self._date = kwargs["date"]
        self._maketitle = kwargs["maketitle"]

    def texify(self, file, indent_level=0):
        head = "\\documentclass[%dpt, %s, %s]{%s}" % (
            self._fontsize,
            self._columns,
            self._titlepage,
            self._type,
        )

        indented_write(file, indent_level, head)
        indented_write(file, indent_level, "\\usepackage[utf8]{inputenc}")
        indented_write(file, indent_level, "\\usepackage{amsmath}")
        indented_write(file, indent_level, "\\usepackage{amssymb}")
        indented_write(file, indent_level, "\\usepackage{graphicx}")
        indented_write(file, indent_level, "\\usepackage{hyperref}")

        for package in self._packages:
            indented_write(file, indent_level, f"\\usepackage{{{package}}}")

        if (self._author or self._title or self._date) and self._maketitle:
            indented_write(file, 0, "")
            indented_write(file, indent_level, f"\\title{{{self._title}}}")
            indented_write(file, indent_level, f"\\author{{{self._author}}}")
            indented_write(file, indent_level, f"\\date{{{self._date}}}")

        indented_write(file, 0, "")


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
        indented_write(file, indent_level, self._text)


###########################################################################################


def make_test_report():
    """Creates a test report."""

    report_kwargs = ReportKwargs(
        author="Albert Einstein",
        title="Annalen der Physik",
        date="",
        maketoc=True,
        maketitle=False,
        type="report",
        titlepage="notitlepage",
    )
    reporter = Reporter("test_report", report_kwargs)

    chapter1        = Segment("The Answer", "chapter1", "chapter")
    section1        = Segment("Intro", "section1", "section")
    subsection11    = Segment("Sub Intro", "subsection11", "subsection")
    section2        = Segment("Main", "section2", "section")
    section3        = Segment("Conclusion", "section3", "section")

    subsection11.add_to_content(PlainText("This is some plain text."))

    section1.add_to_content(subsection11)
    chapter1.add_to_content(section1)
    chapter1.add_to_content(section2)
    chapter1.add_to_content(section3)
    reporter.add_to_document(chapter1)

    reporter.print_structure()
    reporter.report()
