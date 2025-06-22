# String i find()
# 1) Napisz funkcję validate_email sprawdzającą w podstawowy
# sposób czy emial jest prawidłowy.
# 2) Wykorzystaj find() do wyszukiwania fragmentów tekstu w emailu:
# - sprawdź czy istnieje w przekazanym do funkcji emailu
# - znak @, zapisz index monkey_index
# - posiadając pozycję @ sprawdź czy istnieje znak
# kropki po małpie. Zapisz pozycję kropki w dot_index
# - jeżeli wszystkie powyższe warunki są spełnione
# zwróć True, w innym wypadku False
# 3) Wywołaj funkcję z następującymi mailami, pokaż
# w konsoli co zwraca funkcja:
# - asia@example.com
# - karol@domena
# - user.com


def validate_email(email):
    monkey_index = email.find("@")
    if monkey_index == -1:
        return False

    dot_index = email[monkey_index:].find(".")
    if dot_index == -1:
        return False

    return True

print(validate_email("asia@example.com"))
print(validate_email("karol@domena"))
print(validate_email("user.com"))
print(validate_email("arek.szatan@interia.pl"))

