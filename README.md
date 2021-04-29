# Vigenere Cipher
The Vigenere cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, 
based on the letters of a keyword. It employs a form of polyalphabetic substitution.

## Installation
This library uses python3 which can be download from [here](https://www.python.org/). After installing python, use pip to install the package.
```
$ pip install vigenere
```
No external dependencies required in this version.

## Quick Start
Open the python shell and begin encrypting and decrypting texts with only 4 lines of commands.
```python
>>> from vigenere import encrypt, decrypt, random_key
>>> cipher_key:str = random_key() # one can even use user-defined key such as `qwerty`
>>> cipher = encrypt('hello world', cipher_key) # with random_key function, cipher may vary everytime you run a program.
>>> decrypt(cipher, cipher_key)
'hello world'
```

It is noteworthy that the output of the encrypt function is encoded to base64. This can be changed by setting the default argument `base64` to False.

```python
encrypt(..agrs, base64=True) # returns base64 string
encrypt(..args, base64=False) # returns string of unicode chrs
```

Read the documention of the library
```
$ python
Python 3.9.0
Type "help", "copyright", "credits" or "license" for more information.
>>> import vigenere
>>> help(vigenere)
```

## Security
The Vigenere Cipher is not a safe encryption algorithm and has multiple vulnerabilities.

One should not use this library for any official purpose, for its implementation is educational only. If you are downloading this package, it is expected that you have read the documentation and you truly understand the consequences.

I shall not be held responsible if you use this for encrypting confidential documents or messages.

## License
[MIT License](https://raw.githubusercontent.com/GuptaAyush19/Vigenere-Cipher/master/LICENSE)