
num = 0
operation = None
reset = True
result = None
calc_operations = ["+", "-", "*", "/", "**"]

while True:
    if reset:
        num = int(input("Podaj liczbę startową: "))
        reset = False

    operation = input("Podaj operacje arytmetyczną jak np. "
                      + str(calc_operations) + " lub exit jeśli koniec lub reset: ")

    if operation == "exit":
        break

    if operation == "reset":
        reset = True
        continue

    if not operation in calc_operations:
        print("Wprowadzona została błędna operacja.")
        continue

    second_num = int(input("Podaj drugą liczbę: "))

    if operation == "+":
        result = num + second_num

    if operation == "-":
        result = num + second_num

    if operation == "*":
        result = num * second_num

    if operation == "/":
        result = num / second_num

    if operation == "**":
        result = num ** second_num

    print("Wynik operacji " + str(num) + " " + operation
          + " " + str(second_num) + " = " + str(result))

    num = result
    result = None