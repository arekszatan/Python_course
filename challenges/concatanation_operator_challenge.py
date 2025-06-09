# Zadanie do wykonania
# Wykorzystaj operator konkatenacji do łączenia stringów i list,
# oraz zastosuj prostą instrukcje warunkową if.
# 1) Połącz dwa stringi 'first_name' i 'last_name w jeden string 'full_name'
# i wyświetl go. Dodaj między nimi spację.
# 2) Stwórz dwie listy. 'list_one' z liczbami od 1 do 3 i 'list_two' z liczbami
# od 4 do 6. Połącz je w jedna listę 'combined_list' i wyświetl.
# 3) Jeśli długość 'combined_list' jest większa od 5, wyświetl "Lista jest długa".
# 4) Do zmiennej 'greeting' dodaj string 'Hello', a do niej 'full_name'.
# Sprawdź, czy w 'greeting' znajduje się słowo 'Hello'. Jeli tak,
# wyświetl pełne powitanie.

first_name = "Marek"
last_name = "Kowalski"
full_name = first_name + " " + last_name
print(f'full_name is {full_name}')

list_one = [1, 2, 3]
list_two = [4, 5, 6]
combined_list = list_one + list_two
print(f'combined_list is {combined_list}')

if len(combined_list) > 5:
    print("Lista jest długa.")

greeting = "Hello "

greeting += full_name

if "Hello" in greeting:
    print(greeting)