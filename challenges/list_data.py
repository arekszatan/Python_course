# Zadanie: Wyświetlanie listy zakupów
#
# Cel: Napisz program, który tworzy i wyświetla listę zakupów na podstawie
# wprowadzonych przez użytkownika produktów.
# Program nie będzie zwracał żadnej wartości, ale bezpośrednio wyświetli listę zakupów w konsoli.
#
# Kroki do wykonania:
# 1) Zdefinuj funkcję display_shopping_list, która przyjmuje jeden parametr: shopping_list
# Funkcja ta powinna wyświetlać wszystkie elementy listy zakupów, każdy element w nowej linii.
# 2) Stwórz pustą listę zakupów.
# 3) W pętli, poproś użytkownika o wprowadzenie nazw produktów do listy zakupów,
# aż do wypisania słowa "koniec".
# 4) Po zakończeniu wprowadzania, wywołaj funkcję dispay_shopping_list, przekazując jej listę zakupów.

def display_shopping_list(shopping_list):
    for item in shopping_list:
        print(item)

shopping_list = []
running = True

while running:
    product_name = input("Podaj nazwę produktu lub koniec (aby zakończyć): ")

    if product_name == "koniec":
        display_shopping_list(shopping_list)
        running = False

    shopping_list.append(product_name)

print("Koniec działania programu.")

print(" ")

def display_shopping_list_1(shopping_list):
    print("Twoja lista zakupów.")
    for item in shopping_list:
        print(" - ", item)

shopping_list = []

while True:
    product = input("Wpisz kolejny produkt do liste:")
    if product == "koniec":
        break
    shopping_list.append(product)

display_shopping_list_1(shopping_list)