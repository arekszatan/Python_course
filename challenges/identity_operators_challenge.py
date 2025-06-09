# Zadanie do wykonania:
# Wykorzystaj operatory tożsamości (is, is not) do sprawdzenia
# relacji między obiektami
# 1) Stwórz zmienną 'text' z wartością "Hello" i użyj metody upper()
# do wyświetlenia wielkich liter. Sprawdź dostępne metody za pomocą dir()
# 2) Stwórz dwie zmienne 'x' i 'y' z wartością 256. Sprawdź czy x is y.
# 3) Stwórz listę 'list_one' z kilkoma elementami. Skopiuj 'list_one' do 'list_two'
# poprzez przypisanie. Sprawdź, czy list_one is list_two.
# 4) Zmodyfikuj 'list_one' przez ddodanie nowego elementu. Sprawdź, czy zmiania
# wpłynęła na list_two. Użyj if do wyświetlania komunikatu o zmianie.
# 5) Stwórz nową listę 'list_three' z takimi samymi elementami, co 'list_one'.
# Sprawdź, czy list_one is list_three i wyświetl odpowiedni komunnikat z pomocą if.

text = "Hello"
print(text.upper()) # HELLO
print(dir(text))

x, y = 256, 256
print(x is y) # True

list_one = [1, 4, 5, 7, 7]
list_two = list_one
print(list_one is list_two) # True

list_one.append(-1)
print(list_two) # Zmiana list_one wpłynała na zmienę w list_two

if -1 in list_two:
    print("Change in 'list_one' influence on 'list_two'")

list_three = [1, 4, 5, 7, 7, -1]

if list_three is list_one:
    print("'list_three' is 'list_one'")
else:
    print("'list_three is not 'list_one'")
