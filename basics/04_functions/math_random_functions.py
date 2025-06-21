import math
import random

print(type(str(12)))
print(type(int("23")))
print(type(str([12, 34])))

number = int("123")
print(type(number))

number += 10
print(number) # 133
print("123" + "10")

float_num = float("45.67")
print(type(float_num))
float_num = float_num * 2
print(float_num)

print(abs(4))
print(abs(-9))

print(math.ceil(3.14)) # 4
print(math.ceil(3.89)) # 4
print(math.ceil(-2.1)) # -2

print(math.floor(3.14)) # 3
print(math.floor(-2.1)) # -3
print(math.floor(10.67)) # 10
print(math.floor(11.000001)) # 11
print(math.floor(11.999999)) # 11
print(math.floor(5.12)) # 5
print(math.floor(-5.12)) # -6

print(max(10, 1, 33, 89, 0, -1))
print(max([10, 1, 33, 89, 0, -1]))
print(max({10, 1, 33, 89, 0, -1}))
print(min(10, 1, 33, 89, 0, -1))
print(min([10, 1, 33, 89, 0, -1]))
print(min({10, 1, 33, 89, 0, -1}))

print(4 ** 3)
print(pow(4, 3))
print(pow(2, 2))
print(math.sqrt(128))
print(math.sqrt(12))

print(round(12.7893421, 4))
print(round(1.132143, 2))
print(round(1.132143, 0))

print(random.random())
print(random.random() * 100)
print(int(random.random() * 100))

print(random.choice([0, 1, 3, 4, 5]))
print(random.choice(("Ola", "Ania", "Adam")))

print(random.randrange(-10, 30, 5))

list_data = [0, 1, 2, 3, 4, 5, 6]
random.shuffle(list_data)

print(list_data)


