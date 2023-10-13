import os


class classproperty:
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, owner):
        return self.f(owner)
    

#####################################################################


class Switch:
    def __init__(self, name, option1, option2):
        self.name = name
        self.option1 = option1
        self.option2 = option2
        self.current = option1

    def toggle(self):
        if self.current == self.option1:
            self.current = self.option2
        else:
            self.current = self.option1

    def __call__(self):
        return self.current
    

#####################################################################

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
        self.columns = restricted_get(kwargs, "columns", ["onecolumn", "twocolumn"], "onecolumn")
        self.titlepage = restricted_get(kwargs, "titlepage", ["notitlepage", "titlepage"], "notitlepage")
        self.packages = restricted_get(kwargs, "packages", list, [])
        self.author = restricted_get(kwargs, "author", str, None)
        self.title = restricted_get(kwargs, "title", str, None)
        self.date = restricted_get(kwargs, "date", str, "\\today")
        self.maketitle = restricted_get(kwargs, "maketitle", bool, True)
        self.maketoc = restricted_get(kwargs, "maketoc", bool, False)
    
    def get_preamble(self):
        preamble = ""
        preamble += f"\\documentclass[{self.fontsize}pt, {self.columns}, {self.titlepage}]{{{self.type}}}\n"
        preamble += "\\usepackage[utf8]{inputenc}\n"
        preamble += "\\usepackage{amsmath}\n"
        preamble += "\\usepackage{amssymb}\n"
        preamble += "\\usepackage{graphicx}\n"
        preamble += "\\usepackage{hyperref}\n"
        
        for package in self.packages:
            preamble += f"\\usepackage{{{package}}}\n"
        
        preamble += f"\\author{{{self.author}}}\n"
        preamble += f"\\title{{{self.title}}}\n"
        preamble += f"\\date{{{self.date}}}\n"
        
        return preamble

class ReportMaker:
    def __init__(self, report_name, report_kwargs):
        self.report_name = report_name
        self.report_kwargs = report_kwargs
        self.report_contents = "" 

    def add_section(self, section_name):
        self.report_contents += f"\\section{{{section_name}}}\n"

    def add_subsection(self, subsection_name):
        self.report_contents += f"\\subsection{{{subsection_name}}}\n"

    def add_subsubsection(self, subsubsection_name):
        self.report_contents += f"\\subsubsection{{{subsubsection_name}}}\n"

    def add_paragraph(self, paragraph_name, asterisk=False):
        if asterisk:
            self.report_contents += f"\\paragraph*{{{paragraph_name}}}\n"
        else:
            self.report_contents += f"\\paragraph{{{paragraph_name}}}\n"

    def add_equation(self, equation, label=None):
        if label:
            self.report_contents += f"\\begin{{equation}}\n\\label{{eqn:{label}}}\n{equation}\n\\end{{equation}}\n"
        else:
            self.report_contents += f"\\begin{{equation}}\n\n{equation}\n\\end{{equation}}\n"
    
    def make(self):
        try:
            print("Writing report...")
            if not os.path.exists("out"):
                os.mkdir("out")

            with open("out/" + self.report_name + ".tex", "w") as f:
                f.write(self.report_kwargs.get_preamble())
                f.write("\\begin{document}\n")

                if self.report_kwargs.maketitle:
                    f.write("\\maketitle\n")

                if self.report_kwargs.maketoc:
                    f.write("\\tableofcontents\n")

                f.write(self.report_contents)
                f.write("\\end{document}\n")
            
            print("Done!\nCompiling report...")

            os.system(f"latexmk -c -quiet -pdf -outdir=out out/{self.report_name}.tex")

            print("Done!")
        except Exception as e:
            raise ReportError("Report could not be made.") from e

class ReportError(Exception):
    """Raised when report cannot be made."""
    pass


#####################################################################


def restricted_get(kwargs, key, allowed_keys_or_type, default):
    if key in kwargs:
        if isinstance(allowed_keys_or_type, list):
            if kwargs[key] in allowed_keys_or_type:
                return kwargs[key]
            else:
                raise TypeError(f"Value for '{key}' must be one of {allowed_keys_or_type}.")
        elif isinstance(allowed_keys_or_type, type):
            if isinstance(kwargs[key], allowed_keys_or_type):
                return kwargs[key]
            else:
                raise TypeError(f"Value for '{key}' must be of type {allowed_keys_or_type}.")
    else:
        return default


def make_test_report():
    report_kwargs = ReportKwargs(author="Albert Stein", title="Test Report", maketoc=True)
    report_maker = ReportMaker("test_report", report_kwargs)

    report_maker.add_section("Section")
    report_maker.add_subsection("Subsection")
    report_maker.add_subsubsection("Subsubsection")
    report_maker.add_paragraph("Paragraph")
    report_maker.add_paragraph("Paragraph with asterisk", asterisk=True)
    report_maker.add_equation("E = mc^2", label="emc2")

    report_maker.make()