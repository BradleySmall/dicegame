import random


class Die:
    def __init__(self, pips=6, v=None):
        self.pips = pips

        if not v or 1 > v or v > self.pips:
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
        elif isinstance(other, int):
            return self.val == other
        elif isinstance(other, str):
            return str(self.val) == other
        else:
            return False

    def roll(self):
        self.val = random.randint(1, 6)
        return self
