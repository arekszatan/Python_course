# Zadanie: Kalkulator wieku psa w ludzkich latach
#
# Cel: Napisz program, który przelicza wiek psa na ludzkie lata. Program powinien prosić użytkownika
# o wprowadzenie wieku psa, a następnie obliczyć i wyświetlić jego wiek w ludzkich latach.
# Pierwsze dwa lata życia psa liczymy jako 10.5 ludzkiego raku za każdy, a każdy kolejny
#  rok jako 4 ludzkie lata.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję calculate_human_years, która przyjmuje wiek psa jako parametr.
# W funkcji użyj instrukcji if-elif-else do obliczenia wieku psa w ludzkich latach.
# Dla uproszczenia załóżmy, że ilość lat mniejsza równa 2 musi być pomnożona przez 10.5,
# a dla większych wartości od 2 trzeba zastosować działanie 21 + (dog_years - 2) * 4
# 2) Użyj pętli, aby umożliwić użytkownikowi wielokrotne używanie kalkulatora bez
# resetowania programu.
# 3) Poproś użytkownika o wprowadzenie wieku psa.
# 4) Wywołaj funkcję calculate_human_years i przekaż jej wiek psa wprowadzony przez użytkownika.
# 5) Wyświetl obliczony wiek psa w ludzkich latach.

def calculate_human_years(dog_age):
    if dog_age < 0:
        return None

    if dog_age <= 2:
        return dog_age * 10.5
    else:
        return 21 + (dog_age - 2) * 4

running = True

while running:
    dog_age_input = input("Wprowadź wiek psa ('exit' to quit): ")

    if dog_age_input == "exit":
        running = False

    dog_age_in_human_years = calculate_human_years(float(dog_age_input))
    print(f'Wiek psa w ludzkich latach jest równy: {dog_age_in_human_years}')

print("Koniec działania programu.")