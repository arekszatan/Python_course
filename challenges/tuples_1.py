# 1. Stwórz krotke z wartościami: 50, 100, 150, 200, 250
# 2. Pokaż typ krotki w konsoli
# 3. Pokaż w konsoli ilość elementów krotki
# 4. Pokaż ostatni element krotki wykorzystując len() - 1
# 5. Następnie pokaż elementy od drugiego do czwartego
# 6. Pokaż trzeci element od końca z ujemnym indeksem

tuple_example = (50, 100, 150, 200, 250)
print(type(tuple_example))
print(len(tuple_example))
print(tuple_example[len(tuple_example) - 1])
print(tuple_example[2 : 5])
print(tuple_example[-3])