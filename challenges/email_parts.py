# String zadanie:
# 1) Napisz funkcję get_email_parts przyjmującą
# parametr email.
# 2) Wykorzystaj pobieranie fragmentu tekstu na python aby rozłożyć
# email na części i zapisz je w zmiennych.
# - user - od początku emaila do ostatniego znaku przed @
# - domain_name - tekst za @ i przed kropką
# - domain_ext - tests za ostatnią kropką do końca.
# Uwaga: Pamiętaj że określając początek i koniec fragmentu z stringa
# możesz korzystać z zmiennych np:
# monkey_ind = 5
# user = email[0:monkey_ind]
# 3) Zwróć słownik z funkcji z elementami jak powyższe
# zmienne. Pamiętaj aby użyć find aby określić
# pozycję indeksu małpy w email, jeśli go nie ma
# zwróć None z funkcji, podobnie z kropką.
# 4) Przetestuj funkcję na emailu:
# ola@domena.com
# W konsoli powinna pojawić się informacja:
# {'user' : 'ola', 'domain_name' : 'domena', 'domain_ext' : 'com'}

def get_email_parts(email):
    if email.find("@") == -1:
        return None

    if email.find(".") == -1:
        return None

    user = email.split('@')[0]
    rest_of_email = email.split('@')[1]
    domain_name = rest_of_email.split('.')[0]
    domain_ext = rest_of_email.split('.')[1]
    return {
        'user' : user,
        'domain_name' : domain_name,
        'domain_ext' : domain_ext
    }

print(get_email_parts("ola@domena.com"))
print(get_email_parts("oladomena.com"))
print(get_email_parts("ola@domenacom"))
print(get_email_parts("arek.szatan@interia.pl"))