
# operatory tożsamości

str_data = "test"

print(dir(str_data))

print(str_data.upper())

int_data = 10

print(dir(int_data))

a = [1, 2, 3, 4, 5]
b = a

print(a is b)

a.append(77)
print(a)
print(b)
# Te dwie zmienne wskazują na to samo miejsce w pamięci

print(a is not b) # False

c = [3, 4, 5]

print(a is c) # False
print(a is not c) # False
