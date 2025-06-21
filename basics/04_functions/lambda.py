from functools import reduce

sum = lambda x, y: x + y
print(sum(10, 20))

sub = lambda x, y: x - y
print(sub(10, 20))

multiply = lambda x, y: x * y
print(multiply(2, 2))

def generate_lambda(num):
    return lambda a: a * num

doubler = generate_lambda(2)

print(doubler(4))
print(doubler(1))

list_data = [0, 1, 2, 3]
result = list(map(lambda x: x * 3, list_data))
print(result)

print(list(map(lambda x: x / 2, list_data)))

result = list(filter(lambda a: a > 1, list_data))
print(result)

result = reduce(lambda x, y: x + y, "ola", "ania")
print(result)