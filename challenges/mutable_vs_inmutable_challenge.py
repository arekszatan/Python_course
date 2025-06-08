number = 5
addr_number = id(number)
print(f'Place in memory for number is {addr_number}')

number += 2
addr_number_new = id(number)
print(f'Place in memory for number is {addr_number_new}')

fruits = ['apple', 'banana', 'cherry']
addr_of_fruits = id(fruits)
print(f'Place in memory for fruits is {addr_of_fruits}')

fruits.append('orange')
addr_of_fruits_new = id(fruits)
print(f'Place in memory for fruits is {addr_of_fruits_new}')

# Mutable type after change variable don't change place in memory
# Immutable type after change variable change place in memory
# Mutable: list, set, dict
# Immutable: int, float, bool, str, tuple, frozenset