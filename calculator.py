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

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    else:
        return math.log(a, b)

def exponent(a, b):
    return a ** b


