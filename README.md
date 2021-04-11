# Vigenere Cipher
The Vigenere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, 
based on the letters of a keyword. It employs a form of polyalphabetic substitution.

# Installation
This library uses python3 which can be download from [here](https://www.python.org/). After installing python, use pip to install the package.
```
$ pip install vigenere
```
No external dependencies required in this version.

# Quick Start
Open the python shell and begin encrypting and decrypting texts with only 4 lines of commands.
```python
>>> from vigenere import encrypt, decrypt, random_key
>>> cipher_key:str = random_key() # one can even use user-defined key such as `qwerty`
>>> cipher = encrypt('hello world', cipher_key) # with random_key function, cipher may vary everytime you run a program.
>>> decrypt(cipher, cipher_key)
'hello world'
```

Read the documention of the library
```
$ python
Python 3.9.0
Type "help", "copyright", "credits" or "license" for more information.
>>> import vigenere
>>> help(vigenere)
Help on package vigenere:

NAME
    vigenere

DESCRIPTION
    The Vigenere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers,

        ...

    In the 19th century the scheme was misattributed to Blaise de Vigenere (1523-1596), and so acquired its present name.

PACKAGE CONTENTS
    __main__
    random
    vigenere

FUNCTIONS
    decrypt(cipher: str, key: str) -> str
        Decrypt strings using Vigenere Cipher

        Args:
            cipher (str): Encrypted plain text that needs to be decrypted
            key (str): Key for vigenere cipher

        Returns:
            str: Decipher Text

    encrypt(plain_text: str, key: str) -> str
        Encrypt strings using Vigenere Cipher

        Args:
            plain_text (str): Plain text that needs to be encrypted
            key (str): Key for vigenere cipher

            Use `random_key()` to generate a key

-- More  --
```

_WARNING:_ DO NOT USE THIS LIBRARY FOR ANY OFFICIAL PURPOSES, BECAUSE THIS IS FOR EDUCATIONAL USE ONLY. I WILL NOT BE RESPONSIBLE IF YOU USE THIS FOR ENCRYPTING CONFIDENTIAL DOCUMENTS OR MESSAGES.

# License
[MIT License](https://raw.githubusercontent.com/GuptaAyush19/Vigenere-Cipher/master/LICENSE)