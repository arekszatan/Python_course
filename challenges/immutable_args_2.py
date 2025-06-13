# Zadanie: Obliczanie ostatecznej ceny produktu po rabacie
#
# Cel: Napisz program, który oblicza ostateczną cenę produktu po zastosowaniu rabatu.
# Program powinien prosić użytkownika o wprowadzenie ceny początkowej produktu.
# oraz wielkości rabatu w procentach, a następnie obliczyć i wyświetlić cenę końcową.
#
# Kroki do wykonania:
# 1) Napisz funkcję calculate_final_price, która przyjmuje dwa parametry:
# initial_price (cena początkowa produktu) oraz discount (rabat w procentach).
# 2) W funkcji oblicz cenę produktu po rabacie i zwróć tę wartość.
# 3) Poproś użytkownika o wprowadzenie ceny początkowej produktu oraz wielkości rabatu.
# 4) Wywołaj funkcję calculate_final_price z wprowadzonymi wartościami i przechowaj wynik.
# 5) Wyświetl ostateczną cenę produktu.

def calculate_final_price(initial_price, discount):
    final_price = initial_price * (100 - discount) / 100
    return final_price

initial_price_input = float(input("Enter initial price: "))
discount_input = int(input("Enter discount rate (%): "))

final_price_return = calculate_final_price(initial_price_input, discount_input)
print(f'Final price of product is {final_price_return}')