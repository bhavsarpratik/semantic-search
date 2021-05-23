#!/usr/bin/env python
# -*- coding: utf-8 -*-


import io
import os

from setuptools import find_packages, setup

# Package meta-data.
NAME = "semantic_search"
DESCRIPTION = "Make semantic search easier"
URL = "https://github.com/bhavsarpratik/semantic-search"
EMAIL = "pratik.a.bhavsar@gmail.com"
AUTHOR = "Pratik Bhavsar"

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(here, "README.md")) as f:
    long_description = "\n" + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, NAME, "__version__.py")) as f:
    exec(f.read(), about)

# Load requirements file
with open(os.path.join(here, "requirements.txt")) as f:
    INSTALL_PACKAGES = f.read().splitlines()

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=("tests", "notebooks", "data")),
    test_suite="tests",
    include_package_data=True,
    zip_safe=False,  # the package can run out of an .egg file
    install_requires=INSTALL_PACKAGES,
)
