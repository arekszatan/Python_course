# 1. Wykorzystaj funkcje input() wybudowaną w Pythona
#    pobrania informacji od użytkownika z konsoli.
#    Poproś użytkownika o podanie imienia, nazwiska, miasta
#    Zapisz te informacje w zmiennych name surname i city
# 2. Wyświetl w konsoli test podsumowujący pobrane dane:
#    "Nazywasz się Ania Kowalska i miszkasz w mieści: Kraków

print("Podaj imię:")
name = input()

print("Podaj nazwisko:")
surname = input()

print("Podaj misto w jakim mieszkasz:")
city = input()

print(f'Nazywasz się {name} {surname} i miszkasz w {city}')