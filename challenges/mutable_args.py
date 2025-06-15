# Przekazywanie mutowalnych danych do funkcji jak słownik, zadanie:
# 1) Utwórz słownik opisujący pracownika i zapisz go w zmiennej
# employee. Do elementów słownika dodaj:
# name, email, rank (stopień - wpisz programmer), salary (8000)
# 2) Napisz funkcję promote_to_manager, która przyjmuje parametr
# o nazwie user, gdzie przekazywany będzie słownik.
# 3) Wewnątrz funkcji zmień wartość elementu przekazanego
# słownika user, podnieś pensje o 50%, zmień rank
# na managera. Dodatkowo sprawdź, czy przypadkiem przekazany
# pracownik jest już managerem, w takim wypadku podaj w konsoli,
# że osoba ta już jest managerem i wyjdź z funkcji z return.
# 4) Wywołaj funkcję promote_to_manager i przekaż utworzony na początku
# słownik, pokaż w konsoli czy został on zaktualizowany.

def promote_to_manager(user):
    if type(user) is not dict:
        print("Variable user is not a dictionary.")
        return False

    if user["rank"] == "manager":
        print("Promoting to manager is impossible because user is manager.")
        return False

    user["salary"] *= 1.5
    user["rank"] = "manager"

    return True

print("Start of program.")
employee = {
    "name" : "Arek",
    "email" : "arek@example.com",
    "rank" : "programmer",
    "salary" : 8000,
}

if promote_to_manager(employee):
    print("Employee promoted to manager.")
else:
    print("Employee didn't promote to manager.")

print("End of program.")


