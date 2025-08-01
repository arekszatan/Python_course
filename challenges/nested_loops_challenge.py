# Zadanie: Wypisanie elementó∑ z listy list
#
# Cel: Napisz program, który przechodzi przez zagnieżdżoną listę (listę list)
# i wypisuje wszystkie jej elementy.
#
# Kroki do wykonania.
# 1) Stwórz zmienną 'nested_list', która będzie zawierać kilka list z różnymi typami elementów.
# 2) Użyj zagnieżdżonej pętli for do przejścia przez wszystkie listy i ich elementy.
# 3) Wypisz każdy element z każdej listy.
#
# Rozwiązanie:
#
# Definicja zagnieżdżonej listy

nested_lists = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    [True, False, None]
]

for nested_list in nested_lists:
    for v in nested_list:
        print(v)

for sublist in nested_lists:
    for item in sublist:
        print(item)