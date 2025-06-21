# Zadanie: Przetwarzanie danych użytkownika
# Cel: Napisz program do przetwarzania danych użytkowników z listy.
#
# Kroki do wykonania:
# 1) Stwórz listę słowników users, gdzie każdy słownik zawiera klucze 'name' i 'age'
# z przykładowymi danymi użytkownika.
# 2) Użyj filter do wyfiltrowania użytkowników, którzy mają więcej niż 18 lat.
# 3) Użyj map do podwojenia wieku przefiltrowanych użytkowników.
# 4) Użyj reduce do zsumowania wszystkich lad po przetworzeniu.
# 5) Wyświetl sumę lat przefiltrowanych i przetworzonych użytkowników.
#
# Rozwiązanie:

from functools import reduce

users = [
    {'name' : 'Jan', 'age' : 15},
    {'name' : 'Anna', 'age' : 25},
    {'name' : 'Piotr', 'age' : 30},
    {'name' : 'Katarzyna', 'age' : 22}
]

users_result = list(filter(lambda x: x['age'] > 18, users))
print(users_result)

double_age_users = list(map(lambda user: user['age'] * 2, users))
print(double_age_users)

sum_age_users = reduce(lambda x, y: x + y, double_age_users)
print(sum_age_users)

print(" ")

users1 = [
    {'name' : 'Jan', 'age' : 15},
    {'name' : 'Anna', 'age' : 25},
    {'name' : 'Piotr', 'age' : 30},
    {'name' : 'Katarzyna', 'age' : 22}
]

adults = filter(lambda user: user['age'] > 18, users1)

double_ages = map(lambda user: user['age'] * 2, adults)

total_age = reduce(lambda x, y: x + y, double_ages)
print(total_age)
