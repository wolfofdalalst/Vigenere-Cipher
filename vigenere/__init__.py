from .vigenere import *
from .random import randint

with open("vigenere\info.txt", "r") as _info:
    __doc__ = _info.read().strip()
  
__all__ = ["decrypt", "encrypt", "randint", "random_key", "valid_key"]
__author__ = "Ayush Gupta; https://github.com/GuptaAyush19/"
__license__ = "MIT License"
__version__ = "1.0.1"