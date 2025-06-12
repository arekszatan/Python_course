# Zadanie: Wpisywanie liczb parzystych i nieparzystych
#
# Cel: Napisz program, który dla podanego zakresu od 1 do N (gdzie N jest
# wartością wprowadzoną przez użytkownika) wypisze oddzielnie listy liczb
# parzystych i nieparzystych.
#
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie liczby N, która określi zakres.
# 2) Użyj pętli for wraz z funkcją range() do iteracji od 1 do N włącznie.
# 3) Sprawdź za pomocą instrukcji warunkowej, czy aktualnie liczba jest parzysta czy nieparzysta.
# 4) Dodaj liczby parzyste do jednej listy, a nieparzyste do drugiej, możesz stosować append().
# 5) Po zakończeniu iteracji wyświetl obie listy: listę liczb parzystych i listę liczb nieparzystych.
#
# Rozwiązanie:

N = int(input("Wprowadź liczbe N: "))
even_numbers_list = []
odd_numbers_list = []

for value in range(1, N + 1):
    if value % 2 == 0:
        print("Liczba jest parzysta.")
        even_numbers_list.append(value)
    elif value % 2 != 0:
        print("Liczba jest nieparzysta.")
        odd_numbers_list.append(value)

print(f'Lista liczb parzystych: {even_numbers_list}')
print(f'Lista liczb nieparzystych: {odd_numbers_list}')

N = int(input("Podaj górny zakres N: "))

even_numbers = []
odd_numbers = []

for number in range(1, N + 1):
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Parzyste liczby: ", even_numbers)
print("Nieparzyste liczby: ", odd_numbers)


