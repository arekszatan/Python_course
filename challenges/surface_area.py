# Zadanie: Obliczanie pola powierzchni prostokąta
#
# Cel: Napisz program, który oblicza pole powierzchni prostokąta. Program
# powinien prosić użytkownika o wprowadzenie długości i szerokości prostokąta
# a następnie obliczyć jego pole powierzchni.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję calculate_area, która przyjmuje dwa parametry: length i width
# Funkcja ta powinna obliczać pole powierzchni prostokąta i zwracać wynik.
# 2) Poproś użytkownika o wprowadzenie długości prostokąta
# 3) Poproś użytkownika o wprowadzenie szerokości prostokąta
# 4) Wywołąj funkcję calculate_area z wprowadzonymi wartościami i przechowaj wynik.
# 5) Wyświetl wynik obliczeń użytkownikowi.

def calculate_area(length, width):
    return length * width

input_length = float(input("Wprowadź długość prostokąta: "))
input_width = float(input("Wprowadź szerokość prostokąta: "))

result = calculate_area(input_length, input_width)
print(f'Pole powierzchni prostokąta jest równe: {result}')