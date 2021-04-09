from .vigenere import *
from .random import randint

with open("vigenere\info.txt", "r") as _info:
    __doc__ = _info.read().strip()