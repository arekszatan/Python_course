# Zadanie do wykonania
# Wykorzystaj instrukcjie warunkowe do stworzenia prostego programu
# decyzyjnego, analizując wartość zmiennej 'number'.
# 1) Stwórz zmienną 'number' i przypisz jej wartość 15
# 2) Sprawdź, czy 'number' jest większe od 10. Jeśli tak, wyświetl komunikat.
# 3) Sprawdź, czy 'number' jest równe 15. Jeśli tak wyświetl odpowiedni komunikat.
# 4) Użyj 'elif' do sprawdzenia, czy 'number' jest równe 20, 25, lub większe od 30.
# Dla każdego przypadku wyświetl odpowiedni komunikat.
# 5) Jeśli żaden z powyższych waruków nie jest spełniony, użyj 'else' do wyświetlania
# dymyślnego komunikatu.
# 6) Dodaj zagnieżdżoną instrukcję warunkową, aby sprawdzić dodatkowy warunek
# dla jednego z przypadków

number = 15

if number > 10: print("number większy od 10")

if number == 15: print("number równy jest 15")

if number == 20:
    print("number jest równy 20")
elif number == 25:
    print("number jest równy 25")
elif number > 30:
    print("number jest większy od 30")
else:
    print("domyślny komunikat jeżeli żaden z warunków nie jest spełniony")

if number > 10:
    print("number jest większy od 10")
    if 10 > 7:
        print("10 jest większe od 7")
