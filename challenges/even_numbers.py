# 1) Stwórz krotkę z wartościami od 1 do 10
# 2) Zrób pętle for in z krotką i wyświetl w konsoli
# tylko parzyste liczby. Skorzystaj z instrukcji
# warunkowej if oraz operatora % zwracającego resztę
# z dzielenia. Jeśli reszta z dzielenia przez 2
# będzie równa 0 to nie ma reszty, tym samym
# jest parzysta.

krotka = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for k in krotka:
    if k % 2 == 0:
        print(f'Liczba {k} jest liczbą parzystą.')

data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for v in data:
    if v % 2 == 0:
        print(f'Liczba {v} jest liczbą parzystą.')
