# Zadanie na Number:
# 1) Pobierz liczbę całkowitą od użytkownika do zmiennej
# za pomocą funkcji input przekaż do niej informację: Podaj liczbę całkowitą.
# 2) Zmień typ wartości z tekstu na liczbę całkowitą.
# 3) Stwórz funkcję calculate_square_area z parametrami height,
# która zwraca powierzchnie kwadratu.
# 4) Wywołaj funkcję z wcześniej pobraną liczbą całkowitą,
# wynik pokaż w konsoli.
# 5) Pobierz od użytkownika liczbę dziesiętną, pamiętaj o kropce
# w liczbie. Oblicz powierzchnię kwadratu z tą wartością,
# pokaż wynik w konsoli zaokrąglony do 2 miejsc po przecinku.

def calculate_square_area(height):
    return pow(height, 2)

number_int = int(input("Enter a integer number: "))
result_square_1 = calculate_square_area(number_int)
print(f"The square area of {number_int} is {result_square_1}")

number_float = float(input("Enter a float number: "))
result_square_2 = calculate_square_area(number_float)
result_square_2 = round(result_square_2, 2)
print(f'The square area of {number_float} is {result_square_2}')