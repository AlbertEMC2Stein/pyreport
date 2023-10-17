"""pyreport - A Python package for creating LaTeX reports from within your code!"""

from os import path
from ._utils import get_tags

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
