"""Dice module for Die class."""
import random




class Die():


    def __init__(self, pips=6, v=None):
        self.pips = pips

        if not v or v < 1 or v > self.pips:
            v = random.randint(1, self.pips)
        self.val = v

    def __repr__(self):
        return repr(self.val)

    def __int__(self):
        return self.val

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        if isinstance(other, Die):
            return self.val == other.val
        if isinstance(other, int):
            return self.val == other
        if isinstance(other, str):
            return str(self.val) == other
        return False

    def roll(self):
        self.val = random.randint(1, self.pips)
        return self
