import math
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

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b

def mul(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero (argument 'a' was 0).")
    return b / a



def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    else:
        return math.log(a, b)

def log(a, b):
    if a <= 0 or a == 1:
         raise ValueError("Logarithm base 'a' must be positive and not equal to 1.")
    if b <= 0:
         raise ValueError("Logarithm argument 'b' must be positive.")

def exponent(a, b):
    return a ** b

def exp(a, b):
    return a ** b


