
print(bool()) # False

# falsy values, value which give you False after conversion to boolean
print(bool(False)) # False
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(())) # False
print(bool([])) # False
print(bool({})) # False
print(bool('')) # False
print(bool(None)) # False

# truth value, value which give you True after conversion to boolean
print(bool(True)) # True
print(bool(10)) # True
print(bool(-10)) # True
print(bool(-12.43)) # True
print(bool((1, 2, 3))) # True
print(bool([0])) # True
print(bool({0})) # True
print(bool(" ")) # True