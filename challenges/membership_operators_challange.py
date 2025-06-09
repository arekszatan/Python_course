# Zadanie do wykonania:
# Wykorzystaj operatory przynależności (in, not in) do sprawdzenia
# obecności elementów w kolekcjach i użycie instrukcji warunkowej if.
# 1) Sprawdź, czy liczba 7 znajduje się w liście 'numbers' i wyświetl odpowiedni komunikat.
# 2) Sprawdź, czy ciąg znaków "kot" nie znajduje się w tuple 'animals' i wyświetl odpowiedni komunikat.
# 3) Stwórz słownik 'user' z kluczami 'name' i 'age'. Sprawdź, czy klucz 'name' znajduje się w słowniku.

numbers = [1, 3, 5, 7]
print(7 in numbers) # True

if 7 in numbers:
    print("7 w liście")
else:
    print("7 nie jest w liście")

animals = ("kot", "pies", "wąż", "ryba")
print(type(animals)) # <class 'tuple'>
print("kot" not in animals) # False

if "kot" not in animals:
    print("kot nie jest w krotce")
else:
    print("kot jest w krotce")

user = {
    "name" : "Arek",
    "age" : 22
}
print("name" in user.keys())

if "name" in user:
    print("Klucz name jest w słowniku")
else:
    print("Klucza nie ma w słowniku")