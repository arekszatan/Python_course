# Napisz dwie funkcję konwertujące temperaturę:
# 1) Funkcja cToF skonwertuje stopnie Celcjusza na Fahrenheita z wzoru:
# fahreheit = celcius * 9 / 5 + 32
# 2) Funkcja fToC konwertuje stopnie Fahreheita na Celcjusza z wzoru:
# celcius = (fahreheit - 32) * 5 / 9
# 3) Dodatkowo w konsoli pokaż wynik konwersji np:
# "20 stopni Celcjusza to 68 stopni Fahreheita" itd.
# Jeśli chcesz użyj w string specjalnego znaku stopni \xB0
# 4) Skonwertuj 20 celcjuszy na Fahrenheita (68)
# Skonwertuj 86 fahreheita na Celcjusza (30)

def cToF(celcjus):
    return celcjus * 9 / 5 + 32

def fToC(fahreheit):
    return (fahreheit - 32) * 5 / 9

result_fahrenheit = cToF(20)
print(f"20\xB0C to {result_fahrenheit}\xB0F")

result_celcjus = fToC(86)
print(f"86\xB0F to {result_celcjus}\xB0C")
