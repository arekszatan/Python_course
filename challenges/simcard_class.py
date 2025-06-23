# Stwórz klasę SimCard reprezentującą kartę sim telefonu z kontaktami
# 1) Klasa ustawia atrybut/zmienną klasy contacts jako listę w konstruktorze
# 2) Dodaj metodę add_contact przyjmującą oprócz self również parametry
# name i telephone. Sprawdź z funkcją isinstance czy przekazane dane są
# prawidłowe, czyli str i int. Stwórz słownik z name i telephone i dodaj go
# do listy kontaktów obiektu powstałego na bazie klasy.
# 3) Napisz metodę show_contacts, która w pętli pokaże kolejne kontakty w terminalu
# 4) Stwórz instancję klasy SimCard:
# 5) Dodaj poniższe kontakty:
# - "Ola", 928348574
# - "Adam", 384629304
# - 100, 284374638
# - "Kasia". "numer"
# Część danych jest nieprawidłowa, więc nie powinny być dodane przez add_contact
# 6) Wyświetl kontakty z show_contacts()

class SimCard:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, telephone):
        if not isinstance(name, str):
            return False

        if not isinstance(telephone, int):
            return False

        self.contacts.append({
            "name": name,
            "telephone": telephone
        })
        return True

    def get_contact(self):
        return self.contacts

sim = SimCard()
sim.add_contact("Ola", 923847334)
sim.add_contact("Adam", 923847334)
sim.add_contact(100, 923847334)
sim.add_contact("Kasia", "numer")

print(f'All contacts in self.contacts is: ', sim.get_contact())