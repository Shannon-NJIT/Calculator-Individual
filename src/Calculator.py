import math


def addition(x, y):
    z = x + y
    return z

def subtraction(x, y):
    z = y - x
    return z

def multiplication(x, y):
    z = x * y
    return z

class Calculator:
    result = 0

    def __init__(self):
        pass

    def addition(self, x, y):
        self.result = addition(int(x), int(y))
        return self.result

    def subtraction(self, x, y):
        self.result = subtraction(int(y), int(x))
        return self.result

    def multiplication(self, x, y):
        self.result = multiplication(int(x), int(y))
        return self.result


