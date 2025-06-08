
list_data = [1, 2, 3, 4, 5, 6]

tuple_data = tuple(list_data)
print(tuple_data)

other_list = list(("Ola", 23, 433))
print(other_list)

set_data = set(other_list)
print(type(set_data))
print(set_data)

frozen_set_data = frozenset(tuple_data)
print(type(frozen_set_data))
print(frozen_set_data)

tuple_data = (("Ola", 1234), ("Arek", 3421))
dict_data = dict(tuple_data)
print(dict_data)
print(dict_data["Ola"])