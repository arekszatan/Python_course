# immutable: int, float, bool, str, frozenset

def modify_str(str_data):
    print(id(str_data))
    str_data += "!"
    print(id(str_data))
    print(str_data)

string = "Hello"

print(id(string))
modify_str(string)
print(string)

print("")

# mutable types: list, set, dictionary

def modify_list(list_data):
    print(id(list_data))
    list_data.append(10)
    print(id(list_data))

list_value = [0, 1, 2]
print(id(list_value))
print(list_value)

modify_list(list_value)
print(list_value)
