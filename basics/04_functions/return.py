
def add_numbers(a, b, c):
    return a + b + c

def sum_list_elements(list_data):
    if len(list_data) == 0:
        print("Pusta lista!")
        return None
    result = 0
    for v in list_data:
        result += v
    return result

print(sum_list_elements([]))
print(sum_list_elements([1, 2, 3, 4, 5, 6, 7, 8])) # 36

def print_list(list_data):
    if len(list_data) == 0:
        return
    for v in list_data:
        print(v)

print_list([])
print_list([6, 7, 8])



