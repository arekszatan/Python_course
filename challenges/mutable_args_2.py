# Cel: Napisz program, ktøry analizuje wprowadzone temperatury i wykrywa ich średnią.
# najniższą oraz najwyższą wartość. Program powinien prosić użytkownika o wprowadzenie
# temperatur jedna po drugiej, a następnie zwracać raport analizy.
# Komentarze w kodzie będą po polsku, a nazwy zmiennych i funkcji po angielsku.
#
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie serii temperatur, gdzie każda kolejna temperatura jest
# oddzielnie, a zakończenie wprowadzania sygnalizowane jest przez wpisanie 'koniec'.
# 2) Dla każdej wprowadzonej temperatury, dodaj ją do listy temperatur po konwersji na typ float.
# 3) Po zakończeniu wprowadzania danych, wywołaj funkcję analizującą temperatury, która zwraca
# krotkę zawierającą średnią, maksymalną, i minimalną temperature z listy.
# 4) Wyświetl wyniki analizy użytkownika.
#
# Rozwiązanie:

def analyze_temperature(temperature_list):
    if not temperature_list:
        return (0, 0, 0)
    average_temperature = sum(temperature_list) / len(temperature_list)
    max_temperature = max(temperature_list)
    min_temperature = min(temperature_list)
    return (average_temperature, max_temperature, min_temperature)

temperature_list = []
while True:
    temperature = input("Proszę podaj temperaturę ('koniec' aby zakończyć): ")
    if temperature == 'koniec':
        break
    temperature_list.append(float(temperature))

temperature_tuple = analyze_temperature(temperature_list)
print(f'Average temperature in tuple is: {temperature_tuple[0]}')
print(f'Max temperature in tuple is: {temperature_tuple[1]}')
print(f'Min temperature in tuple is: {temperature_tuple[2]}')

print()

def analyze_temperatures(temperatures):
    if not temperature:
        return (0, 0, 0)
    avg_temp = sum(temperatures) / len(temperatures)
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    return (avg_temp, min_temp, max_temp)

temperatures = []
while True:
    temp = input("Wprowadź kolejną temperaturę lub 'koniec' aby zakończyć: ")
    if temp.lower() == 'koniec':
        break
    else:
        temperatures.append(float(temp))

data = analyze_temperatures(temperatures)
avg = data[0]
min = data[1]
max = data[2]

print("avg: ", avg)
print("min: ", min)
print("max: ", max)
