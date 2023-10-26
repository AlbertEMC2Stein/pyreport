"""A module to create LaTeX reports.

This module provides a class to create LaTeX reports. It is based on the
LaTeX document classes 'article' and 'report'. The report is created in the
'out' folder and is compiled with 'latexmk'.
"""

import os

from .document import Document, Preamble
from .errors import ReportError


class Reporter:
    """A class to create LaTeX reports."""

    def __init__(self, report_name, type='report', fontsize=12, columns='onecolumn',
                 titlepage='notitlepage', packages=[], author='', title='',
                 date='\\today', maketitle=True, maketoc=False, save_path='./out',
                 export_pdf=True):
        """Constructor for Reporter.

        Parameters
        ----------
        report_name : str
            Name of report.
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
        assert type in ['article', 'report'], \
            f"Supported types are 'article' and 'report', not {type}"
        assert fontsize in [10, 11, 12], "Invalid fontsize, must be 10, 11 or 12"
        assert columns in ['onecolumn', 'twocolumn'], \
            f"Supported columns are 'onecolumn' and 'twocolumn', not {columns}"
        assert titlepage in ['notitlepage', 'titlepage'], \
            f"Supported titlepages are 'notitlepage' and 'titlepage', not {titlepage}"
        assert isinstance(packages, list), "Packages must be a list"
        assert isinstance(author, str), "Author must be a string"
        assert isinstance(title, str), "Title must be a string"
        assert isinstance(date, str), "Date must be a string"
        assert isinstance(maketitle, bool), "Maketitle must be a boolean"
        assert isinstance(maketoc, bool), "Maketoc must be a boolean"

        self._report_name = report_name
        self._save_path = save_path
        self._export_pdf = export_pdf
        self._report_contents = [
            Preamble(type=type, fontsize=fontsize, columns=columns,
                     titlepage=titlepage, packages=packages, author=author,
                     title=title, date=date, maketitle=maketitle),
            Document(type=type, titlepage=titlepage, title=title, author=author,
                     date=date, maketitle=maketitle, maketoc=maketoc,),
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
            os.makedirs(self._save_path, exist_ok=True)
            file_path = os.path.join(self._save_path, self._report_name + ".tex")

            print(f"Creating the LaTex file: {file_path}")
            with open(file_path, "w", encoding="utf8") as f:
                self._report_contents[0].texify(f)
                self._report_contents[1].texify(f)
            print("Done!")

            if self._export_pdf:
                print("Compiling the PDF...")
                os.system(f"latexmk -cd -pdf -quiet {file_path}")
                os.system(f"latexmk -cd -c {file_path}")
                print("PDF created!")
        except Exception as e:
            raise ReportError("Report could not be made.") from e

    def print_structure(self):
        """Prints the structure of the report."""
        print("Report structure:")
        print(self._report_contents[1].get_structure())
