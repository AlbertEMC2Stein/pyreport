from setuptools import setup, find_packages
import subprocess
from sys import executable, version
from os.path import split
from os import chmod
from PyReport import get_info

###########################################################

with open('requirements.txt') as f:
    requirements = list(f.read().splitlines())

package_info = get_info()

setup(
    name=package_info['name'],
    version=package_info['version'],
    description=package_info['description'],
    url=package_info['url'],
    author=package_info['author'],
    author_email=package_info['author_email'],
    license=package_info['license'],
    python_requires='>=3.9',
    packages=find_packages(include=['eSPAy']),
    install_requires=requirements
)

# script = f"""#!/bin/sh
# '''exec' "{executable}" "$0" "$@"
# ' '''
# # -*- coding: utf-8 -*-
# import re
# import sys
# from PyReport.__main__ import cli_entry
# if __name__ == '__main__':
#     sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
#     sys.exit(cli_entry())
# """

# with open(f'{split(executable)[0]}/PyReport', 'w') as f:
#     f.write(script)

# chmod(f'{split(executable)[0]}/PyReport', 448)