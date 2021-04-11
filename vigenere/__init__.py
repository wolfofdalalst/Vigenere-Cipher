from .vigenere import *
from .random import randint

__doc__ = """The Vigenere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, 
based on the letters of a keyword. It employs a form of polyalphabetic substitution.

First described by Giovan Battista Bellaso in 1553, the cipher is easy to understand and implement, but it 
resisted all attempts to break it until 1863, three centuries later. This earned it the description le 
chiffre indechiffrable (French for 'the indecipherable cipher'). Many people have tried to implement encryption 
schemes that are essentially Vigenere ciphers. In 1863, Friedrich Kasiski was the first to publish a general 
method of deciphering Vigenere ciphers.

In the 19th century the scheme was misattributed to Blaise de Vigenere (1523-1596), and so acquired its present name."""
  
__all__ = ["decrypt", "encrypt", "randint", "random_key", "valid_key"]
__author__ = "Ayush Gupta; https://github.com/GuptaAyush19/"
__license__ = "MIT License"
__version__ = "1.0.3"