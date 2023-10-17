import os
from abc import ABC, abstractmethod
from ._utils import restricted_get, indented_write

__all__ = ["ReportKwargs", "Reporter", "ReportError", "make_test_report"]

###########################################################################################


class ReportKwargs:
    def __init__(self, **kwargs):
        """A class to hold the arguments for the report.

        Parameters
        ----------
        type : "article"|"report", optional
            Type of report, by default "report"
        fontsize : 10|11|12, optional
            Font size, by default 12
        columns : "onecolumn"|"twocolumn", optional
            Number of columns, by default "onecolumn"
        titlepage : "notitlepage"|"titlepage", optional
            Title page, by default "notitlepage"
        packages : list, optional
            List of packages to import, by default []
        author : str, optional
            Author of report, by default None
        title : str, optional
            Title of report, by default None
        date : str, optional
            Date of report, by default "\\today"
        maketitle : bool, optional
            Make title, by default True
        maketoc : bool, optional
            Make table of contents, by default False
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
        self.author = restricted_get(kwargs, "author", str, None)
        self.title = restricted_get(kwargs, "title", str, None)
        self.date = restricted_get(kwargs, "date", str, "\\today")
        self.maketitle = restricted_get(kwargs, "maketitle", bool, True)
        self.maketoc = restricted_get(kwargs, "maketoc", bool, False)

    def to_dict(self):
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
    def __init__(self, report_name, report_kwargs):
        self._report_name = report_name
        self._report_contents = [
            Preamble(**report_kwargs.to_dict()),
            Document(**report_kwargs.to_dict()),
        ]

    def add_to_document(self, obj):
        self._report_contents[1].add_to_content(obj)

    def report(self):
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


class ReportError(Exception):
    """Raised when report cannot be made."""


###########################################################################################


class Environment(ABC):
    @abstractmethod
    def __init__(self, name):
        self._name = name
        self._contents = []

    @abstractmethod
    def texify(self, file, indent_level=0):
        pass

    def add_to_content(self, obj):
        assert not isinstance(obj, Document), "Cannot add Document to Environment."
        self._contents.append(obj)

    def print_structure(self, indent_level=0):
        result = f"{self._name}\n"
        for content in self._contents:
            if isinstance(content, Environment):
                result += indent_level * "   " + f"|-- {content.print_structure(indent_level + 1)}"

    def __str__(self):
        return f"Environment: {self._name:<12}"


class Document(Environment):
    def __init__(self, name="document", **kwargs):
        super().__init__(name)
        self._type = kwargs["type"]
        self._titlepage = kwargs["titlepage"]
        self._maketitle = kwargs["maketitle"]
        self._maketoc = kwargs["maketoc"]

    def texify(self, file, indent_level=0):
        indented_write(file, indent_level, "\\begin{document}")
        indented_write(file, indent_level + 1, "\\maketitle\n" if self._maketitle else "", end="")

        # small hack because those two options interfere with each other
        toc_command = r"\tableofcontents"
        if self._titlepage == "notitlepage" and self._type == "report":
            toc_command = r"{\let\clearpage\relax\tableofcontents}"

        indented_write(file, indent_level + 1, toc_command + "\n" if self._maketoc else "")

        for content in self._contents:
            content.texify(file, indent_level + 1)

        indented_write(file, indent_level, "\\end{document}")


class Section(Environment):
    def __init__(self, name, label, asterisk=False):
        super().__init__(name)
        self._label = label
        self._asterisk = asterisk

    def texify(self, file, indent_level=0):
        asterisk = "*" if self._asterisk else ""
        indented_write(file, indent_level, f"\\section{asterisk}{{{self._name}}}")
        indented_write(file, indent_level, f"\\label{{sec::{self._label}}}")

        for content in self._contents:
            content.texify(file, indent_level + 1)

        indented_write(file, 0, "")


###########################################################################################


class LatexObject(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def texify(self, file, indent_level=0):
        pass

    def __str__(self):
        return f"LatexObject: {self._name:<12}"


class Preamble(LatexObject):
    def __init__(self, name="preamble", **kwargs):
        super().__init__(name)
        self._type = kwargs["type"]
        self._fontsize = kwargs["fontsize"]
        self._columns = kwargs["columns"]
        self._titlepage = kwargs["titlepage"]
        self._packages = kwargs["packages"]
        self._author = kwargs["author"]
        self._title = kwargs["title"]
        self._date = kwargs["date"]

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

        indented_write(file, indent_level, f"\n\\author{{{self._author}}}")
        indented_write(file, indent_level, f"\\title{{{self._title}}}")
        indented_write(file, indent_level, f"\\date{{{self._date}}}\n")


class PlainText(LatexObject):
    def __init__(self, text):
        super().__init__("plaintext")
        self._text = text

    def texify(self, file, indent_level=0):
        indented_write(file, indent_level, self._text)


###########################################################################################


def make_test_report():
    report_kwargs = ReportKwargs(
        author="Albert Stein", title="Test Report", 
        maketoc=True, type="article", titlepage="notitlepage"
    )
    reporter = Reporter("test_report", report_kwargs)

    section1 = Section("Section 1", "section1", asterisk=True)
    section2 = Section("Section 2", "section2")
    section3 = Section("Section 3", "section3")

    section3.add_to_content(PlainText("This is some plain text."))

    reporter.add_to_document(section1)
    reporter.add_to_document(section2)
    reporter.add_to_document(section3)

    reporter.report()
