# Zadanie: Filtracja i przetwarzanie listy
#
# Cel: Napisz program, który przechodzi przez listę liczb całkowitych od 1 do 10,
# pomija liczby parzyste, zatrzymuje się, gdy napotka liczbę większą niż 8,
# a dla pozostałych liczb wypisuje ich kwadrat.
#
# Kroki do wykonania:
# 1) Stwórz listę liczb całkowitych od 1 do 10.
# 2) Użyj pętli for do integracji przez listę.
# 3) W pętli użyj instrukcji 'continue' do pominięcia liczb parzystych.
# 4) Użyj instrukcji 'break' do zakończenia pętli, gdy liczba jest większa niż 8.
# 5) Dla liczb nieparzystych mniejszych lub równych 8 wypisz ich kwadraty.
# 6) Na końcu pętli użyj instrukcji 'else' do wypisania komunikatu o zakończeniu przetwarzania.
#

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers_list:
    if number % 2 == 0:
        continue

    if number > 8:
        break

    if number % 2 != 0 and number <= 8:
        print(number ** 2)
else:
    print("Koniec działania pętli.")

print("")

numbers = list(range(1, 11))

for i in numbers:
    if i > 8:
        break

    if i % 2 == 0:
        continue

    print("Kwadrat liczby: ", i ** 2)
else:
    print("Zakończenie pętli.")
