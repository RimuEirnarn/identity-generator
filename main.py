"""Main File

This main file generates simplest ID code for a character or anything.
"""

from secret import SystemRandom as _SystemRandom
from random import Random as _Random
from random import randint as _randbase

base_10 = list("1234567890")
base_26 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def generator(sep="-", order=[base_26, base_10]):
    """The Generator

    Argument:
      sep: is used to be a seperator between base-26 and base-10
           for example AA-0000.
      order: used to be how it generates. (ex. AA-AA-5000, then
             the order will be: [base_26, base_26, base_10]"""
    pass


# Offerides from GTRN.util.randint
def randint(x, y, onion=3):
    """a Random Integer Generator.
    
    This Function. creates an random integer and use it as seed. the process will still continue, until "onion" (another name of Layer) reached 0 or lesser."""
    base = _randbase(x, y)
    base_ = None
    default_onion = onion
    while onion > 0:
        n = _randbase(0, 10)
        if not base_:
            if n <= 5:
                base_ = _Random(base).randint(x, y)
            if n > 5 and n <= 10:
                base_ = _SystemRandom(base).randint(x, y)
        else:
            if n <= 5:
                base_ = _Random(base_).randint(x, y)
            if n > 5 and n <= 10:
                base_ = _SystemRandom(base_).randint(x, y)
        onion -= 1
    if default_onion <= 0:
        base_ = randint(x, y, 3)  # Default
    return base_
