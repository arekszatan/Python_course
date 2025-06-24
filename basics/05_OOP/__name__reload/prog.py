import math_module
import importlib

print(math_module.add_numbers(10, 2))
print("prog.py: " + __name__) # główny plik zawsze ma __main__

importlib.reload(math_module)
print(" ")
importlib.reload(math_module)
