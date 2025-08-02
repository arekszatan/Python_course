# import modułu unitest, który jest wbudowany w Pythona i służy
# do testowania jednostkowego
import unittest

# definicaj funkcji add, która będzie testowanya
def add(x, y):
    return x + y

# Dodatkowa funkcja substract do testowania
def subtract(x, y):
    return x - y

# Definicja klasy testowej ArithmeticOperationTest, która dziedziczy po unittest.TestCase
# Test Case jest podstawową klasą unittest, służącą do tworzenia przypadków testowych
class ArithmeticOperationsTest(unittest.TestCase):

    # Metoda testowa test_add, któ©a sprawdza poprawnośc działania funckji add.
    # Nazwa metody zawsze powinna zaczynać się od słowa "test"
    def test_add(self):
        # Wywołanie metody assertEqual, aby sprawdzić czy wynik
        # funkcji add jest równy oczekiwanej wartosci.
        # assertEqual przyjmuje dwa argumenty: pierwszy to wynik funkcji,
        # drugi to oczekiwana wartość.
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    # Metoda testowa test_subtract, która sprawdza, czy funkcji subtract
    # poprawnie oblicza różnice między podanymi liczbami.
    def test_subtract(self):
        # Sprawdzenie, czy wynik funkcji subtract jest zgodnyt z oczekiwaniami.
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

# Warunek sprawdzający, czy skrypt został uruchominy bezpośrednio,
# a nie zaimportowany jako moduł.
# Jeśli tak, to uruchamina jest funkcja unittest.main(), któ©a odpowiada
# za uruchamianie wszystkich testów zdefiniowanych w klasie.
if __name__ == "__main__":
    unittest.main()
