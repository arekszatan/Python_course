# Zadanie: Rezerwacja biletów na koncert
#
# Cel: Napisz program, który pozwoli użytkownikowi zarezerwować bilety na koncert.
#
# Kroki do wykonania:
# 1) Zdefiniuj funkcję book_tickets, która przyjmuje nazwę zespołu jako argument
# pozycyjny (band), liczbę biletów jako argument pozycyjny, a rodzaj biletów i sekcję
# jako argumenty nazwane z domyślnymi wartościami jako standard i general.
# 2) Funkcja powinna wyświetlać informacje o rezerwacji, włączając w to wszystkie
# podane detale.
# 3) Poproś użytkownika o wprowadzenie nazwy zespołu i liczby biletów,
# następnie tylko je przekaż przy wywołaniu funkcji.
#

def book_tickets(band_name, number_of_tickets, /, *, type_of_tickets = "standard", section = "general"):
    print(f'Band name: {band_name}')
    print(f'Number of tickets: {number_of_tickets}')
    print(f'Type of tickets: {type_of_tickets}')
    print(f'Section name: {section}')

band_name = input("Enter band name: ")
number_of_tickets = int(input("Enter number of tickets:"))

book_tickets(band_name, number_of_tickets)