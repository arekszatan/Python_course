
# Zadanie - operacje na rachunku bankowym, skorzystaj
# z skróconych operatorów przypisania z operacją
# matematyczną np: += -= *= /= itd
# Uwaga, po każdej operacji wyświetl saldo w konsoli
# 1) Stwórz zmienną balance z wartością początkową 1000
# 2) Dodaj wartość nowej pensji 7000
# 3) Odejmij 2000 kosztów na mieszkanie
# 4) Błąd banku pomnożył Twoje saldo trzykrotnie
# 5) Odejmij 4000 na komputer
# 6) Bank zoorientował się że powstał błąd i cofa ostatnie
# transakcjie. Dodaj do salda 4000, podziel je przez 3
# i dopiero teraz odejmij 4000
# 7) Pokaż saldo

balance = 1000
print(f'Value of bank account is: {balance}')

balance += 7000
print(f'Value of bank account is: {balance}')

balance -= 2000
print(f'Value of bank account is: {balance}')

balance *= 3
print(f'Value of bank account is: {balance}')

balance -= 4000
print(f'Value of bank account is: {balance}')

balance += 4000
balance /= 3
balance -= 4000
print(f'Value of bank account is: {balance}')

