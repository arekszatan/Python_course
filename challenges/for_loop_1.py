# Liczby nieparzyste dodane do set
# 1) Dodaj listę numbers z wartościami od -3 do 3 z krokiem co 1
# 2) Dodaj set z wartością początkową -1
# 3) Stwórz pętlę for in z tablicą numbers
# 4) W każdej iteracji pętli sprawdź czy liczba z listy jest nieparzysta,
# czyli reszta z dzielenia przez dwa nie może być równa zero (!= 0)
# Dodaj nieparzystą liczbę do zestawu.
# 5) Wyświetl w konsoli nieprzyste liczby w set za pomocą pętli for

numbers = [-3, -2, -1, 0, 1, 2, 3]
set_data = {-1}

for value in numbers:
    if value % 2 != 0: # value jest nieparzyste
        set_data.add(value)

for value in set_data:
    print(f'Value is {value}')
