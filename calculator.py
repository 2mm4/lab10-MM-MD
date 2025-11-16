#https://github.com/2mm4/lab10-MM-MD
#Partner 1: Melanie Morgado
#Partner 2: Matthew Doyle

import math

def square_root(a):
        if a < 0:
            raise ValueError
        else:
            return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (argument 'a' was 0).")
    return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    else:
        return math.log(b, a)

def exp(a, b):
    return a ** b


