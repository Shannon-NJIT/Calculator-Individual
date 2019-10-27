import math


def addition(x, y):
    z = x + y
    return z


class Calculator:
    result = 0

    def __init__(self):
        pass

    def addition(self, x, y):
        self.result = addition(int(x), int(y))
        return self.result
