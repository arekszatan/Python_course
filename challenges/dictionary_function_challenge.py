# Zadanie - zarządzanie książką adresową
# W tym zadaniu będziesz używać słowników do zarządzania prostą
# książką adresową. Nauczysz się dodawać, usuwać, kopiować oraz
# przeszukiwać dane w słowniku.
#
# 1) Stwórz słownik 'address_book zawierający początkowo jedną
# osobę: Jan Kowalski, mieszka w Gdańsku, kod pocztowy 80-000.
# 2) Dodaj do książki adresowej nową osobę: Anna Nowak, mieszka w
# Warszawie, kod pocztowy 00-001.
# 3) Usuń Jan Kowalski z książki adresowej.
# 4) Skopiuj książkę adresową do nowej zmiennej i sprawdź, czy
# kopia jest identyczna (porównaj referencje i zawartość).
# 5) Sprawdź, czy w skopiowanej książce adresowej jest osoba
# mieszka w Krakowie. Jeśli nie, wyświetl odpowiedni komunikat.
# 6) Wyświetl wszystkie klucze i wartości w książce adresowej.

address_book = {
    "Jan Kowalski" : {"city" : "Gdańsk", "postal_code" : "80-000"}
}
print("Początkowa wartość książki adresowej: ", address_book)

address_book["Anna Nowak"] = {"city" : "Warszawa", "postal_code": "00-001"}
print("Książka po aktualizacji", address_book)

del address_book["Jan Kowalski"]
print("Książka po skasowaniu elementu: ", address_book)

address_book_copy = address_book.copy()
print("Czy zawartość jest identyczna: ", address_book_copy == address_book)
print("Czy referencje są identyczne: ", address_book is address_book_copy)

found = False
for person in address_book.values():
    if person["city"] == "Kraków":
        found = True
        print("W książce adresowej jest osoba z Krakowa.")

if not found:
    print("W książce adresowej nie ma osoby z Krakowa.")

print("Klucze: ", address_book.keys())
print("Klucze: ", address_book.values())