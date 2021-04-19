"""Main File

This main file generates simplest ID code for a character or anything.
"""

from secret import SystemRandom as _sysrand
from random import Random

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

