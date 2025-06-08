# 1.Stwórz set z unikalnymi wartościami jak:
#   Ania, Kasia, Ola, Karol, Daniel, Zuza
# 2.Dodaj do set za pomocą funkcji add kolejne elementy
#   Olek, Basia, Kasia, Karol, Zuza, Paulina
# 3. Pokaż w konsoli wielkość set
# 4.Wykorzystaj pętlę for aby pokazać elementy w set

names_set = {"Ania", "Kasia", "Ola", "Karol", "Daniel", "Zuza"}
names_set.add("Olek")
names_set.add("Basia")
names_set.add("Kasia")
names_set.add("Karol")
names_set.add("Zuza")
names_set.add("Paulina")

print(f'Size of names_set is {len(names_set)}')

for name in names_set:
    print(f'Name of names_set is {name}')