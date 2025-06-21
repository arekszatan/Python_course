# Zadanie: Kalkulator średniej arytmetycznej
#
# Cel: Napisz program kalkulatora, który oblicza średnią arytmetyczną z listy liczb.
# Program powinien używać funkcji lambda, map oraz reduce do przetworzenia listy liczb
# i obliczania wyniku. Zadanie ma na celu praktyczne zastosowanie wyrażenia lambda
# i funkcji wyższego rzędu do przetwarzania danych.
#
# Kroki do wykonania:
# 1) Zdefiniuj listę liczb, dla której ma zostać obliczona średnia arytmetyczna.
# 2) Użyj funkcji map i lambda do przekształcenia listy liczb, jeśli to konieczne.
# 3) Wykorzystaj funkcję reduce i lambda do obliczania sumy wszystkich liczb z listy.
# 4) Oblicz średnią arytmetyczną dzieląc sumę przez ilość liczb w liście.
# 5) Wyświetl wynik.
#
# Rozwiązanie:

from functools import reduce

number_list = [0.1, 2, 5, 6, 1, 10, -1]

number_list = list(map(lambda x: x * 2, number_list))
print(f'Number list after multiplication is {number_list}')

number_list_sum = reduce(lambda x, y: x + y, number_list)
average = number_list_sum / len(number_list)
print(f'The average is: {average}')