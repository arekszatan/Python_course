# Zadanie - symulacja kosztów podróży
# W tym zadaniu skorzystasz z funkcji matematycznych i losowych
# do symulacji kosztów podróży. Użyj danych typów, funkcji matematycznych
# oraz funkcji z modułu random do wyliczania i przewidzenia kosztów.
#
# 1) Stwórz zmienną 'distance' z losową wartością od 100 do 1000, która
# oznacza dystans w kilometrach do pokonania.
# 2) Oblicz spodziewane spalanie na podróż, przyjmując, że na 100 km
# spala się 7 litrów paliwa. Użyj zaokrąglenia w górę.
# 3) Przyjmij cenę paliwa za litr jako losową wartość zmiennoprzecinkową
# między 4.5 a 5.5. Zaokrąglij cenę do dwóch miejsc po przecinku.
# 4) Oblicz całkowity koszt paliwa na podróż.
# 5) Jeśli koszt paliwa przekracza 400 zł, wyświetl komunikat o wysokich
# kosztach podróży. W przeciwnym razie, poinformuj o przystępnych kosztach.
import math
import random

distance = random.randint(100, 1000)
print(distance)

fuel_consumption_per_100km = 7
expected_fuel_consumption = math.ceil(distance / 100) * fuel_consumption_per_100km

fuel_price = round(random.uniform(4.5, 5.5), 2)

total_cost = round(expected_fuel_consumption * fuel_price, 2)
print("Koszt: ", total_cost)

if total_cost > 400:
    print("Wysokie koszty podróży")
else:
    print("Koszty akceptowalne")
