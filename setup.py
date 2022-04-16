#

from setuptools import setup
import sys

setup(
    name="yamlviewer",
    version="2.0",
    packages=["yamlviewer"],
    install_requires=[
        "PySide2",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "yamlviewer=yamlviewer.yamlviewer:main",
        ],
    },
)


