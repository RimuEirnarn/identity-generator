"""Main File

This main file generates simplest ID code for a character or anything.
"""

from secrets import SystemRandom as _SystemRandom
from random import Random as _Random
from random import randint as _randbase

base_10 = list("1234567890")
base_26 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
base_36 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

def generator(sep="-", order=[base_26, base_10], order_max=[2, 4], order_min=[1, 1]):
    """The Generator

    Argument:
      sep: is used to be a seperator between base-26 and base-10
           for example AA-0000.
      order: used to be how it generates. (ex. AA-AA-5000, then
           the order will be: [base_26, base_26, base_10])
      order_max: used to be the maximum characters for every order.
           (ex. [2, 4] then the order arg. would look like this
           [base_26, base_10], and rougly returns like this
           AA-0000)
      order_min: used to be the minimum characters for every order."""
    ret = [[] for a in order_max]
    for ord_mx in order_max:
        index = order_max.index(ord_mx)
        ord_mn = order_min[index]
        base = order[index]
        ln = randint(ord_mn, ord_mx)
        while ln != 0:
            ret[index].append(base[randint(0, len(base))])
            ln -= 1

    string = ""
    for a in ret:
        string += "".join(b for b in a)
        string += "-"
    string = string[:-1]
    return string


# Offerides from GTRN.util.randint
def randint(x, y, onion=3):
    """a Random Integer Generator.
    
    This Function. creates an random integer and use it as seed. the process will still continue, until "onion" (another name of Layer) reached 0 or lesser."""
    base = _randbase(x, y)
    base_ = None
    default_onion = onion
    if x == y:
        return x
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
