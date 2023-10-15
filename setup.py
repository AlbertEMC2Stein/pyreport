from setuptools import setup, find_packages
from sys import executable, version
from os.path import split
from os import chmod
from pyreport import get_info

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
    packages=find_packages(include=['pyreport']),
    install_requires=requirements
)