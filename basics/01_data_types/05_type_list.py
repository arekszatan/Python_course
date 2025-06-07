
list_example = ["Ola", "Ania", 23, 99, "Rafał"]
print(type(list_example))
print(list_example)

print(list_example[0])
print(len(list_example))
print(list_example[4])
print(list_example[len(list_example) - 1])
# print(list_example[5]) # IndexError: list index out of range
print(list_example[-1])
print(list_example[-2])
# print(list_example[-6]) # IndexError: list index out of range

print(list_example[1:4])
print(list_example[2:])

list_example[0] = "Arek"
print(list_example)

del list_example[4]
print(list_example)

print(99 in list_example)
print("Ania" in list_example)
print(10 in list_example)

if "Ania" in list_example:
    print("Ania is in list list_example")
    print("Next code")

print("Continue code")

for element in list_example:
    print(element)

data = [
    ["Daniel", "Rafał"],
    ["Kasia", "Ania"],
    ["Ola", "Adam"]
]
print(len(data))

print(data[1][0])
print(data[2][1])
print(data[0])

data1 = [1, 2, 3]
data2 = [3, 5, 6]

numbers = data1 + data2
print(numbers)

numbers_x2 = numbers * 2
print(numbers_x2)