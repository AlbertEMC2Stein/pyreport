"""pyreport - A Python package for creating LaTeX reports from within your code!"""

import os.path as path
from os import listdir

def _get_tags():
    def get_creation_time(item):
        item_path = path.join('.git/refs/tags', item)
        return path.getctime(item_path)

    items = listdir('.git/refs/tags')
    sorted_items = sorted(items, key=get_creation_time)
    return sorted_items

_tags = _get_tags()

if len(_tags) == 0:
    _latest_tag = "0.0.0"
else:
    _latest_tag = str(_tags[-1])[1:]

#######################################################

ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))

def get_info():
    return {
        "name": "pyreport",
        "version": _latest_tag,
        "description": __doc__,
        "url": "https://github.com/AlbertEMC2Stein/pyreport",
        "author": "Tim Prokosch",
        "author_email": "prokosch@rhrk.uni-kl.de",
        "license": "TBA"
    }

__all__ = ['get_info']