# Zadanie: Zarządzanie stanem konta użytkownika.
#
# Cel: Napisz program do zarządzania stanem konta użytkownika, który pozwala na
# dodawanie i usuwanie środków oraz wyświetlanie aktualnego stanu konta. Program
# powinien korzystać z globalnej zmiennej do przechowywania stanu konta oraz
# zawierać funkcję do modyfikacji tego stanu i wyświetlania go.
#
# Korki do wykonania:
# 1) Zdefiniuj globalną zmienną account_balance z wartością początkową 0.
# 2) Napisz funkcję add_funds, która przyjmuje kwotę do dodania do konta.
# Funkcja ta powinna modyfikować globalną zmienną account_balance
# 3) Napisz funkcje withdraw_funds, która przyjmuje kwotę do wypłaty z konta.
# Sprawdź czy stan konta pozwala na wypłatę - jeśli nie, wyświetl odpowiedni komunikat.
# 4) Napisz funkcję display_balance, która wyświetla aktualny stan konta.
# 5) Zapytaj użytkownika w pętli o działanie (dodanie środków, wypłata, wyświetlanie stanu)
# i odpowiednio zareaguj, wywołując odpowiednią funkcję.
#
# Rozwiązanie:

account_balance = 0

def add_found(amount):
    global account_balance
    account_balance += amount

def withdraw_found(amount):
    global account_balance
    if account_balance < amount:
        print("The amount in the account is smaller than the amount you want to cash out.")
        return False
    account_balance -= amount
    return True

def display_balance():
    print("The amount in the account is: ", str(account_balance))

running = True
while running:
    action = input("What would you like to do (add, withdraw, display, exit): ")
    if action == "add":
        amount = int(input("Enter the amount to be added: "))
        add_found(amount)
    elif action == "withdraw":
        amount = int(input("Enter the amount to be withdrawn: "))
        withdraw_found(amount)
    elif action == "display":
        display_balance()
    elif action == "exit":
        running = False
    else:
        print("Invalid input. Please try again.")

