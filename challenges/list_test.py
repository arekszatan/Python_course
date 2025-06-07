
number_list = [0, 1, 2, 3, 4, 5, 6]
print(f'Length of number_list is {len(number_list)}')

del number_list[0:2]
print(f'Length of number_list is {len(number_list)}')

if 3 in number_list:
    print(f'The number 3 is in the list number_list')
else:
    print(f'The number 3 is not in the list list_numbers')

for element in number_list:
    print(f'The element {element} is in the list number_list')

for element in number_list:
    print(f'The element times 2 is {element * 2}')
