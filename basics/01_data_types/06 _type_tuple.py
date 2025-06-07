
data = ("Ala", "Ola", "Kasia")
# data[0] = "Rafał" # TypeError: 'tuple' object does not support item assignment

names = data + ("Rafał",)
print(names)
print(len(names))
print(type(names))

numbers = 1, 2, 3
print(type(numbers))

emptyTuple = ()
print(type(emptyTuple))

print(names[1])
print(names[-1])
print(names[1:3] * 2)

cars = (("dodge", "ford"), ("pontiak", "opel"))
print(cars[0][0])

if "ford" in cars[0]:
    print(f'Ford in tuple')

# del cars[0][0]
# print(cars)