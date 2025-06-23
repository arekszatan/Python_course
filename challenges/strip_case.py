#
# Funkcje String:
# 1) Napisz funkcję get_user_information z trzema parametrami:
# name, surname, job
# 2) W get_user_information zmień imię i nazwisko na duże litery.
# zawód na małe, dodatkowo wyczyść te wartości
# z białych znaków na ich początku i końcu
# 3) Połącz imię i nazwisko wraz z innym tekstem aby uzyskać tekst np:
# "imię: ANIA, nazwisko: KOWALSKA, zawód: testerka"
# 4) Zwróć powstały tekst z funkcji.
# 5) Wywołaj funkcję get_user_information na następujących
# danych i pokaż je w konsoli:
# - Ania, Kowalska, Programistka
# - Danie, Lis, Administrator

def get_user_information(name, surname, job):
    name = name.upper().strip()
    surname = surname.upper().strip()
    job = job.lower().strip()
    return_string = "imię: " + name + ", nazwisko: " + surname + ", zawód " + job
    return return_string

print(get_user_information("Ania ", "Kowalska ", "Programistka"))
print(get_user_information("Daniel  ", "Lis", "Administrator"))