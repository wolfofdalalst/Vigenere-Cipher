import pathlib
from setuptools import setup, find_packages
from vigenere import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="vigenere",
    version=__version__,
    description="Encrypt strings using Vigenere Cipher",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/GuptaAyush19/Vigenere-Cipher",
    author="Ayush Gupta",
    author_email="darthvader01502@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "realpython=vigenere.__main__:main",
        ]
    },
)