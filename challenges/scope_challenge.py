# Pracownicy w liście z zwiększoną pensją
# 1) Stwórz globalną zmienną employees, która jest pustą listą
# 2) Napisz funkcję add_employee, która przyjmuje email i salary, wewnątrz stwórz
# słownik z tymi samymi parametrami. Następnie dodaj go do globalnej listy
# employees stosując funkcję append np some_list.append(new_element)
# 3) Wywołaj funkcję add_employee dla trzech dowolnych pracowników
# o pensjach: 6000, 8000 i 10000, wpisz dowolne maile
# 4) Dodaj funkcję increase_salary z dwoma argumentami: employees i pct_increase
# Jako pierwszy argument będzie przekazywana lista pracowników, a do drugiego
# wartość podwyżki np. 15 Przejdź po wszystkich pracownikach i zwiększ
# pensję pracowników o przekazaną wartość procentową pct_increase
# 5) Zwiększ pensje pracowników z funkcją increase_salary o 20%, wyświetl
# listę w terminalu

employees = []

def add_employee(email, salary):
    employee_dict = {
        "email" : email,
        "salary" : salary
    }
    employees.append(employee_dict)

add_employee("example1@com", 6000)
add_employee("example2@com", 8000)
add_employee("example3@com", 10000)

def increase_salary(employees, pct_increase):
    for employee in employees:
        employee["salary"] += employee["salary"] * pct_increase / 100

increase_salary(employees, 20)

print("employees list: ", employees)