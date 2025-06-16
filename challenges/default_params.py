#
# Funkcja z domyślnymi wartościami parametrów
# 1) Napisz funkcję z parametrami:
# - email
# - country z domyślą wartością "Polska"
# - company z domyślą wartością "Example Ltd"
# 2) Zwróć z funkcji słownik z elementami jak parametry
# 3) Przetestuj funkcję z jednym argumentem ol@example.com
# oraz drugi przypadek z kasia@example.com będąca z UK

def user_information(email, country ="Polska", company ="user@example.com"):
    return {
        "email" : email,
        "country" : country,
        "company" : company
    }

print(user_information("ola@example.com"))
print(user_information("kasia@example.com", "UK"))