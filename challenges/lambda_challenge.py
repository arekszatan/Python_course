# Zadanie z lambdą i map
# 1) Stwórz listę names z wartościami: Ola, Ania, Kasia
# 2) Z pomocą mapy i lambda dodaj do każdego imienia tekst " Kowalska"
# 3) Wyświetl nową listę w konsoli.
# 4) Przefiltruj nową listę ze względu na długość tekstu, zachowaj
# w nowej liście tylko te, które mają więcej niż 12 znaków.
# Pokaż przefiltrowaną listę w konsoli.

names = ["Ola", "Ania", "Kasia"]

result_1 = map(lambda x: x + " Kowalska", names)
result_1 = list(result_1)
print(f'New list is {result_1}')

result2 = filter(lambda x: len(x) > 12, result_1)
print(f'New list is {list(result2)}')