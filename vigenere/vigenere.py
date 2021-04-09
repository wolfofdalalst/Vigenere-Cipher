from .random import randint

def valid_key(key: str):
    """Checks if the user-key is valid, otherwise returns True

    Raises:
        TypeError, Warning

    Returns: True
    
    >>> from vigenere import valid_key
    >>> valid_key('qwerty')
    True
    >>> valid_key(420)
    Traceback (most recent call last):
        ...
    TypeError: The key must be of type string
    >>> valid_key('foo')
    Traceback (most recent call last):
        ...
    Warning: Please use a much stronger key of length > 5
    """
    if type(key) is not str:
        raise TypeError("The key must be of type string")
    if len(key) <= 5:
        raise Warning("Please use a much stronger key of length > 5")
    
    return True

def random_key(key_size: int = 20) -> str:
    """Return a random key of length `key_size`"""
    if type(key_size) is not int or key_size <= 0:
        raise TypeError("The key size must be a positive integer")
    key_list = [chr(randint(43, 122)) for _ in range(key_size)]
    return "".join(key_list)

def _transform(string:str, key:str, mode = "encrypt") -> str:
    key_index:int = 0
    transform_text:str = ""
    
    if type(string) is not str:
        raise TypeError("The input text must be string")
    
    for char in string:
        if mode.startswith("en"):
            transform_text += chr(ord(char)+ord(key[key_index]))
                
        elif mode.startswith("de"):
            transform_text += chr(ord(char)-ord(key[key_index]))
        else:
            print(mode)
            raise TypeError("Not a valid arguement for `mode`")  
        if key_index - 1 == len(key):
            key_index = 0
            
    return transform_text

def encrypt(plain_text: str, key:str) -> str:
    """Encrypt strings using Vigenere Cipher

    Args:
        plain_text (str): Plain text that needs to be encrypted
        key (str): Key for vigenere cipher
        
        Use `random_key()` to generate a key

    Returns:
        str: Cipher Text
    """
    return str(_transform(plain_text, key, mode="encrpyt"))

def decrypt(cipher: str, key: str) -> str:
    """Decrypt strings using Vigenere Cipher

    Args:
        cipher (str): Encrypted plain text that needs to be decrypted
        key (str): Key for vigenere cipher

    Returns:
        str: Decipher Text
    """
    return str(_transform(cipher, key, mode="decrypt"))