# Stwórz funkcje do konwersji czasu
# 1) 'convert_to_second' przyjmująca ilość godzin
# oraz minut i zwracająca ilość sekund.
# Jako parametry funkcji zapisz: hours, minutes.
# Skonwertuj 3 godziny i 25 minut na sekundy,
# wynik pokaż w konsoli.
# 2) convert_to_hours przyjmującą parametry minutes
# oraz zwracając ilość godzin.
# Skonnwertuj 120 minut na godziny i pokaż
# wynik w konsoli.

def convert_to_seconds(hours, minutes):
    return hours * 60 * 60 + minutes * 60

print("Ilość sekund to: " + str(convert_to_seconds(3, 25)))

def convert_to_hours(minutes):
    hours = int(minutes / 60)
    minutes %= 60
    return hours, minutes

print("Ilość (godzin, minut) to: " + str(convert_to_hours(120)))
print("Ilość (godzin, minut) to: " + str(convert_to_hours(110)))


