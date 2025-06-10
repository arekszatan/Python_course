# Zadanie: Obliczanie średniej arytmetycznej
#
# Cel: Napisz program, który oblicza średnią arytmetyczną z podanej przez użytkownika
# listy liczb. Program powinien prosić użytkownika o wprowadzenie liczby elementów
# do obliczania średniej, a następnie o wprowadzenie każdej z tych liczb.

# Kroki do wykonania:
# 1) Poproś użytkownika o wprowadzenie liczby elementów, z których ma być obliczona średnia.
# 2) Zainicjuj zmienną 'sum' wartością 0, która będzie przechowywać sumę wprowadzonych liczb.
# 3) Użyj pętli while do pobrania od użytkowanika określonej liczby elementów. Po wprowadzeniu
# każdej liczby dodaj ją do zmiennej 'sum'.
# 4) Oblicz średnią arytmetyczną, dzieląc sumę przez liczbę elementów.
# 5) Wyświetl wynikową średnią arytmetyczną z dokładnością do dwóch miejsc po przecinku.
# 6) Jeśli użytkownik wprowadzi liczbę elementów równą 0, wyświetl informację, że nie można
# obliczyć średniej z 0 elementów.

try:

    numbers_of_elements_in_dict = input("Proszę podaj liczbę elementów tabliczy liczb:")
    counter = int(numbers_of_elements_in_dict) - 1
    dictionary = []
    sum = 0

    while counter >= 0:
        dictionary_value = input("Podaj liczbę do tablicy liczb:")
        dictionary.append(int(dictionary_value))
        sum += int(dictionary_value)
        counter -= 1

    average = sum / int(numbers_of_elements_in_dict)

    print(f'Średnia arytmetyczna dla tablicy {dictionary}'
          f' dla {numbers_of_elements_in_dict} elementów is {average}')

except ValueError as e:
    print(e)

print("------------------")

number_of_elements = int(input("Podaj licznę elementów: "))

sum = 0

if number_of_elements > 0:
    i = number_of_elements

    while i > 0:
        i -= 1
        num = float(input("Podaj liczbę: "))
        sum += num

    average = sum / number_of_elements
    print("Średnia:", average)
else:
    print("Nie można obliczyć średniej")
