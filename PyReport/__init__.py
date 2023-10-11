"""PyReport - A Python package for creating LaTeX reports from within your code!"""

import os.path as path
import git

_repo = git.Repo('.git')
_tags = sorted(_repo.tags, key=lambda t: t.commit.committed_datetime)

if len(_tags) == 0:
    _latest_tag = "0.0.0"
else:
    _latest_tag = str(_tags[-1])[1:]

#######################################################

print("PyReport version", _latest_tag)

ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))

def get_info():
    return {
        "name": "PyReport",
        "version": _latest_tag,
        "description": __doc__,
        "url": "https://github.com/AlbertEMC2Stein/PyReport",
        "author": "Tim Prokosch",
        "author_email": "prokosch@rhrk.uni-kl.de",
        "license": "TBA"
    }