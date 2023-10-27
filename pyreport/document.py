"""A module to hold the LaTeX document environment and preamble."""

from .base import Environment, LaTeXObject
from .utils import indented_write


class Document(Environment):
    """A class to hold the LaTeX document environment."""

    def __init__(self, name="document", type="report", titlepage="notitlepage",
                 title="", author="", date="\\today", maketitle=True, maketoc=False):
        """Constructor for Document.

        Parameters
        ----------
        name : str, optional
            Name of document, by default "document".
        type : str, optional
            Type of document, by default "report".
        titlepage : str, optional
            Titlepage option, by default "notitlepage".
        title : str, optional
            Title of document, by default "".
        author : str, optional
            Author of document, by default "".
        date : str, optional
            Date of document, by default "\\today".
        maketitle : bool, optional
            Whether to make a title, by default True.
        maketoc : bool, optional
            Whether to make a table of contents, by default False.
        """

        super().__init__(name)
        self._type = type
        self._titlepage = titlepage
        self._title = title
        self._author = author
        self._date = date
        self._maketitle = maketitle
        self._maketoc = maketoc

    def texify(self, file, indent_level=0):
        indented_write(file, indent_level, "\\begin{document}")

        if (self._title or self._author or self._date) and self._maketitle:
            end = "\n" if self._maketitle else ""
            indented_write(
                file, indent_level + 1, "\\maketitle" if self._maketitle else "", end=end
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


class Preamble(LaTeXObject):
    """A class to hold the LaTeX preamble."""

    DEFAULT_PACKAGES = [
        ("inputenc", "utf8"),
        "amsmath",
        "amssymb",
        "graphicx",
        "hyperref",
        "booktabs",
    ]

    def __init__(self, type="report", fontsize=12, columns="onecolumn",
                 titlepage="notitlepage", packages=[], author='', title='',
                 date='\\today', maketitle=True):
        """Constructor for Preamble.

        Parameters
        ----------
        name : str, optional
            Name of preamble, by default "preamble".
        **kwargs : dict
            Arguments for preamble.
        """
        super().__init__("preamble")
        self._type = type
        self._fontsize = fontsize
        self._columns = columns
        self._titlepage = titlepage
        self._packages = set(self.DEFAULT_PACKAGES + packages)
        self._author = author
        self._title = title
        self._date = date
        self._maketitle = maketitle

    def texify(self, file, indent_level=0):
        head = "\\documentclass[%dpt, %s, %s]{%s}" % (
            self._fontsize,
            self._columns,
            self._titlepage,
            self._type,
        )

        indented_write(file, indent_level, head)
        for package in self._packages:
            if isinstance(package, tuple):
                package, options = package
                indented_write(file, indent_level, f"\\usepackage[{options}]{{{package}}}")
            else:
                indented_write(file, indent_level, f"\\usepackage{{{package}}}")

        if (self._author or self._title or self._date) and self._maketitle:
            indented_write(file, 0, "")
            indented_write(file, indent_level, f"\\title{{{self._title}}}")
            indented_write(file, indent_level, f"\\author{{{self._author}}}")
            indented_write(file, indent_level, f"\\date{{{self._date}}}")

        indented_write(file, 0, "")
