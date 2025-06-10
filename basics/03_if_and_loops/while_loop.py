
number = 5

while number > 0:
    print(number)
    number -= 1 # number = number - 1

number = 1

while number < 6:
    print(number)
    number += 1

num = 0

while True:
    print("Wprowadź liczbę lub 'exit' aby zakończyć działanie programu.")
    str_data = input()
    if str_data == "exit": break
    try:
        num += int(str_data)
        print("Wartość po dadaniu liczby: " + str(num))
    except ValueError:
        print("Podana wartość w 'str_data' nie można przekonwertować na integer.")

number = 3
while number > 0:
    print(number)
    number -= 1
else:
    print("Number po pętli: " + str(number))
