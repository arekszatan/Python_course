# Zadanie - klasa do tworzenia pizzy
# Stworzysz teraz prostą klasę Pizza, która pozwoli na tworzenie
# obiektu pizza i listy składników.
#
# 1) Zdefiniuj klasę Pizza z konstruktorem (__init__), który tworzy
# atrybut 'ingredients' (składniki), będący pustą listą na start.
# 2) Dodaj metodę 'add_ingredient', która przyjmuje jeden parametr.
# (oprócz self) - składnik (ingredient) do dodania do pizzy.
# Sprawdź, czy składnik jest typu str, jeśli tak - dodaj go do listy.
# 3) Dodaj metodę 'show_ingredients', która wyświetla wszystkie
# składniki pizzy.
# 4) Stwórz instancję klasy Pizza.
# 5) Dodaj składniki do pizzy używając metody 'add_ingredient':
# 'ser', 'pomidor', 'pieczarki'.
# 6) Wyświetl składniki pizzy wywołując metodę show_ingredients.

class Pizza:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        if not isinstance(ingredient, str):
            print("Ingredient must be a string!")
            return
        self.ingredients.append(ingredient)

    def show_ingredients(self):
        print(f'All ingredients is: {self.ingredients}')

pizza1 = Pizza()
pizza1.add_ingredient("ser")
pizza1.add_ingredient("pomidor")
pizza1.add_ingredient("pieczarki")
pizza1.show_ingredients()