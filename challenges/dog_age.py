# Zadanie: Kalkulator wieku psa na ludzkie lata
#
# Cel: Napisz program, który przelicza wiek psa na ludzkie lata
#
# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie wieku psa w latach i zapisz tę wartość do zmiennej
# 2) Użyj instrukcji warunkowych, aby obliczyć wiek psa w ludzkich latach.
# - Pierwszy rok życia psa to 15 ludzkich lat. human_age = dog_age * 15
# - Drugi rok życia psa to kolejne 9 ludzkich lat. human_age = 15 + (dog_age - 1) * 9
# - Każdy kolejny rok to 5 ludzkich lat. 24 + (dog_age - 2) * 5
# 3) Jeśli podana wartośc wieku psa jest mniejsza niż 0, wyświetl komunikat o błędzie.
# 4) Wyświetl wynik obliczeń w konsoli.

print("Podaj wiek psa: ")

try:
    dog_age = float(input())
    human_age = 0

    if 1 >= dog_age > 0:
        human_age = dog_age * 15
    elif 2 >= dog_age > 1:
        human_age = 15 + (dog_age - 1) * 9
    elif dog_age > 2:
        human_age = 24 + (dog_age - 2) * 5
    elif dog_age <= 0:
        print("Błąd, wiek psa nie spełnia warunków, wiek musi być dodatni.")

    if human_age > 0:
        print(f'Wiek psa w ludzkich latach jest równy: {human_age}')

except ValueError:
    print("Wiek psa musi być liczbą.")

