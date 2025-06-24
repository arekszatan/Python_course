import random

def add_numbers(a, b):
    print("math_module: " + __name__)
    return a + b

print(__name__, "random int: ", random.randint(0, 100))