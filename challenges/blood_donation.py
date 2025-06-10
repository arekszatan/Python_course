# Program ma na celu kwalifikację kandydatów do oddania krwi
# 1) Dodaj zmienną age o wartości 18 oraz weight = 50
# 2) Napisz instrukcję if else sprawdzającą czy kandydat
# ma wiek większy lub równy 18, jeśli tak sprawdź kolejną
# instrukcje if else czy jego waga jest większa lub równa 50.
# Jeśli oba warunki są spełnione napisz w konsoli że może
# oddać krew
# 3) W przypadku gdy jakiś warunek nie jest spełniony to po else
# napisz w konsoli dlaczego

age = 18
weight = 50

if age >= 18:
    print(f'Kandydat do oddania krwi spełnia warunek wieku, ma {age} lat.')
    if weight >= 50:
        print("Kandydat spełnia warunek wieku i warunek wagi, waga jest równa " + str(weight) + " kg")
    else:
        print("Waga kandydata jest za niska aby oddać krew.")
else:
    print("Kandydat jest za młody na oddanie krwi")

