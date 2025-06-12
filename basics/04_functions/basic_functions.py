
def add_number(num1, num2):
    return num1 + num2

def sub_number(num1, num2):
    return num1 - num2

def multiply_number(num1, num2):
    return num1 * num2

def add_4_numbers(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    return result

print(add_number(10, 5))

number = sub_number(100, 56)
print(number)

number = multiply_number(33, 4)
print(number)

sum = add_4_numbers(1, number, add_number(10, 6), sub_number(10, 1))
print(sum)

