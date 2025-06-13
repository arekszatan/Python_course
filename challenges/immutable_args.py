# Zadanie na przekazanie danych funkcji przez wartość
# 1) Napisz funkcję increase_salary z dwoma parametrami
# liczbowymi: money oraz bonus
# 2) W funkcji podnieś wartość money o 20%.
# Następnie zwróć sumę money oraz bonus.
# 3) Stwórz zmienną salary poza funkcją o wartości 5000.
# 4) Wywołaj funkcje increase_salary przekazując jako
# argumenty salary oraz 1000 jako bonus. Zachowaj
# zwracaną wartość w zmiennej new_salary
# 4) Pokaż w konsoli wartości: salary i new_salary,
# ponieważ przekazywane dane są niemutowalne to salary
# musi mieć wartość 5k, a new_salary odpowiednio większą\
# według implementacji funkcji.

def increase_salary(money, bonus):
    money *= 1.2
    return money + bonus

salary = 5000
new_salary = increase_salary(salary, 1000)

print(f'Salary is equal to {salary}')
print(f'New salary is equal to {new_salary}')