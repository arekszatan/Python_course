# Zadanie: Tworzenie profilu użytkownika
#
# Cel: Napisz program, któ®y umożliwia utworzenie profilu użytkownika w systemie.
# Program powinien prosić użytkownika o podanie imienia, nazwiska, wieku oraz
# miasta pochodzenia. Nie wszystkie informacje są wymagane. Użyj funkcji z nazwanymi
# argumentami.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję create_user_profile przyjmującą argumenty: first_name, last_name
# age oraz city
# 2) Funkcja powinna zwracać słownik zawierający informacje o profilu użytkownika.
# 3) Poproś użytkownika o wprowadzenie wymaganych danych.
# 4) Wywołaj funkcję create_user_profile z odpowiednimi argumentami wprowadzonymi przez
# użytkownika i przechowaj zwrócony słownik.
# 5) Wyświetl zwrócony profil użytkownika.
#
# Rozwiązanie:

def create_user_profile(first_name, last_name, age, city):
    return {
        "first_name" : first_name,
        "last_name" : last_name,
        "age" : age,
        "city" : city
    }

first_name_input = input("Please enter your first name: ")
last_name_input = input("Please enter your last name: ")
age_input = input("Please enter you age: ")
if age_input:
    age_input = int(age_input)
city_input = input("Please enter your city: ")

# if first_name_input:
user_profile = create_user_profile(first_name = first_name_input,
                                   last_name = last_name_input,
                                   age = age_input,
                                   city = city_input)

print(f'User profile is: {user_profile}')