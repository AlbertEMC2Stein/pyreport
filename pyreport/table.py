import pandas as pd

from .base import LaTeXObject
from .utils import indented_write


class Table(LaTeXObject):
    """ Class to hold LaTeX tables.
    
    Tables can be created from pandas DataFrames.
    """
    
    def __init__(self, data, name="table", caption="", label=""):
        """Constructor for Table.

        Parameters
        ----------
        data : pandas.DataFrame or str
            Data to hold. If str, then it is assumed to be a path to a .csv-file.
        name : str, optional
            Name of table, by default "table".
        caption : str, optional
            Caption of table, by default "".
        label : str, optional
            Label of table, by default "".
        """
        super().__init__(name)
        assert isinstance(data, (str, pd.DataFrame)), \
            "Data must be a pandas.DataFrame or a path to a .csv-file."

        self._data = data
        self._caption = caption
        self._label = label
        if isinstance(data, str):
            self._data = pd.read_csv(data)

    def texify(self, file, indent_level=0):
        tex = "\\begin{table}[ht]\n"
        tex += "\t\\centering\n"

        lines = self._data.to_latex(index=False).split("\n")[:-1]
        for i, line in enumerate(lines):
            bodyindent = "\t" if i not in [0, len(lines) - 1] else ""
            tex += "\t" + bodyindent + line + "\n"

        tex += f"\t\\caption{{{self._caption}}}\n" if self._caption else ""
        tex += f"\t\\label{{tab:{self._label}}}\n" if self._label else ""
        tex += "\\end{table}\n"
        indented_write(file, indent_level, tex)
