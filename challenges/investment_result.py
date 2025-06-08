# 1) Oblicz zwrot z investycji po roku, zapisz poniższe zmienne:
#    - capiton - 5000
#    - rate_of_interest - 0.08 czyli 8%
#    - inflation_rate - 0.15 czyli 15%
# 2) Oblicz zwrot z investycji oraz o ile spadła wartość
#    kapitału z uwagi na inflację, pokaż te kwoty w konsoli
# 3) Dodaj do kapitału zwwrot z inwestycji oraz odejmnij
#    utracony kapitał z uwagi na inflację, pokaż wartość końcową w konsoli

capital = 5000  # kapitał
rate_of_interest = 0.08  # odsetki
inflation_rate = 0.15  # iflacja

earned_money = capital * rate_of_interest
print(f'After year interest is {earned_money}')

lost_money = capital * inflation_rate
print(f'After year lost that amount of money {lost_money}')

new_capital = capital + earned_money - lost_money
print(f'Final amount is {new_capital}')

