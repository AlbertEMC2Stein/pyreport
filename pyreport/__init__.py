"""pyreport: Automate Your LaTeX Reports with Python 📝

Create elegant LaTeX reports effortlessly from your code with pyreport. Generate and populate reports with plots, tables, custom environments, commands, and structure, all within your Python environment. Say goodbye to LaTeX headaches and focus on your work while pyreport handles the document creation for you.

- Automate LaTeX Reporting: Generate LaTeX reports seamlessly during your computations.
- Dynamic Content: Add plots, tables, variable logs, and custom LaTeX elements effortlessly.
- Structure Your Report: Define sections, chapters, and more for a well-organized document.
- Focus on Your Work: Stop worrying about LaTeX intricacies and focus on your data and analysis.

Simplify your report creation process with pyreport. No LaTeX expertise required.
"""

from os import path
from .utils import get_tags

__all__ = ["get_info"]

ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
TAGS = get_tags(ROOT_DIR)
LATEST_TAG = "0.0.0"

if len(TAGS) > 0:
    LATEST_TAG = str(TAGS[-1])[1:]

#######################################################


def get_info():
    """Get the package information."""

    return {
        "name": "pyreport",
        "version": LATEST_TAG,
        "description": __doc__,
        "url": "https://github.com/AlbertEMC2Stein/pyreport",
        "author": "Tim Prokosch",
        "author_email": "prokosch@rhrk.uni-kl.de",
        "license": "TBA",
    }
