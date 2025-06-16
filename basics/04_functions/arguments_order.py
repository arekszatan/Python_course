
def print_car(brand, /, name = "concept", *, year = 1960, color = "black"):
    print(brand, name, year, color)

print_car("Ford", "Mustang", year = 1973, color = "red")
print_car("Ford", "Mustang", color = "red",year = 1973 )

# '/' - wszystkie parametry w funkcji przed muszą być pozycyjne, czyli ma być
# zachowana kolejność i nie mogą być to parametry nazwane.
# '*' - wszystkie parametry za muszą być przekazane jako parametry nazwane