from secrets import randbelow as _randbelow

def randint(a: int, b: int) -> int:
    """Return a random integer in the range [a, b] \n
    using secrets module in the standard library.
    """
    if not all(isinstance(i, int) for i in [a, b]):
        raise ValueError("Must be an integer")
    return _randbelow(b-a+1)+a