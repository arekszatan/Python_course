# Zadanie - zarządzanie kontem użytkownika
# W tym zadaniu stworzysz prostą klasę reprezentującą konto użytkownika.
# Będziesz zarządzać podstawowymi informacjami o użytkowniku oraz umożliwić zmianę hasła
#
# 1) Stwórz klasę User, która w konstruktorze przyjmuje dwa parametry:
# username (nazwę użytkownika) i password (hasło), Zapisz te wartości jako atrybuty obiektu.
# 2) Dodaj metodę change_password, która przyjmuje dwa argumenty:
# old_password (stare hasło) i new_password (nowe hasło). Sprawdź czy stare hasło
# zgadza się z obecnym hasłem użytkownika. Jeśli tak, zmień hasło na nowe.
# 3) Stwórz instancję klasy User z przykładowym użytkownikiem.
# 4) Spróbuj zmienić hasło użytkownika za pomocą metody change_password.
# Najpierw użyj nieprawidłowego starego hasła, a następnie prawidłowego.

class User:
    def __init__(self, username, password):
        print("Creating new user.")
        self.username = username
        self.password = password

    def change_password(self, old_password, new_password):
        if old_password != self.password:
            print("Wrong password!")
            return False

        self.password = new_password
        print("Password changed successfully!")
        return True

user1 = User("Kasia", "1234")
user1.change_password("123213", "213123")
user1.change_password("1234", "2342334")