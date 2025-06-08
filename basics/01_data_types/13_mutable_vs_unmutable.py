
# immutable: int, float, bool, str, tuple, frozenset
# Function id to get place in memory

a = 1
addr1 = id(a)

a += 1
addr2 = id(a)

print(addr1)
print(addr2)
print(addr1 == addr2)

# mutable types: list, set, dict
list_data = [0, 1, 2]
addr1 = id(list_data)

list_data += [3, 4, 5]
addr2 = id(list_data)

print(addr1)
print(addr2)
print(addr1 == addr2)
