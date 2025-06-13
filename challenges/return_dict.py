# Zadanie z zwracanym słownikiem użytkownika
# 1) Stwórz funkcje creat_user z parametrami:
# - name
# - contact
# 2) W ciele funkcji stwórz zmienną user, w której będzie
# słownik reprezentujący użytkownika. Dodaj do słownika
# nazwę użytkownika z parametru.
# 3) Parametr contact będzie mógł przyjąć tekst lub liczbę
# Sprawdź za pomocą funkcji isinstance jaki typ ma
# przekazany parametr contact. Jeżeli jest to typ string
# to poniższy kod zwróci wartość True dla zmiennej contact
# isinstance(contact, str). Wtedy zakładamy, że jest to
# adres email, który przypiszesz do słownika użytkownika.
# Natomiast jeśli contact jest liczbą to zakładamy, że
# jest to telefon, więc zapisz element telephone
# w zwracanym słowniku użytkownika. Do sprawdzenia czy
# contact jest liczbą użyj isinstance(contact, int)
# 4) Wywołaj funkcję z dwoma przypadkami:
# - imię Ola, contact (string): ola@example.com
# - imię Kasia, contact (number): 987654321
# Pokaż w konsoli zwrócone słowniki

def create_user(name, contact):
    second_key = None
    if isinstance(contact, str): # email
        second_key = "email"
    elif isinstance(contact, int): # telephone number
        second_key = "telephone"
    user = {
        "name" : name,
        second_key : contact
    }
    return user

print(create_user("Ola", "ola@example.com"))
print(create_user("Kasia", 987654321))

def create_user_1(name, contact):
    user = {
        "name" : name,
        "email" : None,
        "telephone" : None
    }

    if isinstance(contact, str):
        user["email"] = contact
    elif isinstance(contact, int):
        user["telephone"] = contact

    return user

print(create_user_1("Ola", "ola@example.com"))
print(create_user_1("Kasia", 987654321))

