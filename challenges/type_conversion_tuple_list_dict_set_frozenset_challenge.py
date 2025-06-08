
numbers = [7, 8, 9, 10, 11, 12]
print(f'List numbers is {numbers}')

numbers_tuple = tuple(numbers)
print(f'Type of numbers_tuple is {type(numbers_tuple)}')
print(f'Value of numbers_tuple is {numbers_tuple}')

mixed_list = ["Arek", 34, 2134.12, (34, 56)]
print(f'Mixed list mixed_list have {mixed_list}')

mixed_set = set(mixed_list)
print(f'Mixed sed has {mixed_set} and has type {type(mixed_set)}')

frozen_set_numbers = frozenset(numbers_tuple)
print(f'type of frozen_Set_numbers is {type(frozen_set_numbers)}')
print(f'Value of frozen_set_numbers is {frozen_set_numbers}')

name_age_pairs = (("Arek", 32), ("Ola", 22), ("Marek", 34))
name_age_pairs_dict = dict(name_age_pairs)
print(f'Value of name_age_pairs_dict has {name_age_pairs_dict}')
print(f'Value for marek is {name_age_pairs_dict["Marek"]}')
