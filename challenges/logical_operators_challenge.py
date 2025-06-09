# Zadanie do wykonania
# Wykorzystaj operatory logiczne (and, or, not) do sprawdzenia
# różnych warunków i wyświetl odpowiednie komunikaty w konsoli.
# 1) Sprawdź jednocześnie, czy zmienna 'hours_worked' z wartością 9 jest większa od 8 i czy
# 'project_finished' z True jest True. Jeśli tak, wyświetl "Możesz iść do domu".
# 2) Sprawdź, czy temperatura 'temp' jako 35 jest mniejsza od 0 lub większa od 30
# Jeśli tak, wyświetl "Ekstremalne warunki pogodowe".
# 3) Użyj operatora not, aby sprawdzić czy 'is_holiday' z False czy jest False.
# Jeśli tak, wyświetl "Dziś jest dzień roboczy".
# 4) Użyj kombinacji operatorów, aby sprawdzić, czy 'errors_found' z 12 jest
# mniejsze od 10 i czy 'warnings' z 1 jest równe 0. Jeśli nie, wyświetl
# "Sprawdź kod jeszcze raz".

hours_worked = 9
project_finished = True

if hours_worked > 8 and project_finished:
    print("Możesz iść do domu")

temp = 35

if temp < 0 or temp > 30:
    print("Ekstremalne warunki pogodowe")

is_holiday = False

if not is_holiday:
    print("Dziś jest dzień roboczy")

error_found = 12
warnings = 1



if not(error_found < 10 and warnings == 0):
    print("Sprawdź kod jeszcze raz")