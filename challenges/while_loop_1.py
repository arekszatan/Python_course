# Skorzystaj z pętli while aby dodać wartości od 1 do 100
# 1) Dodaj zmienną i równą 0, która będzie inkrementowana w pętli o 1
# Kolejną zmienną będzie sum z wartością początkową 0
# 2) W pętli dodaj do sum wartość i, następnie
# zrób inkrementację i o jeden
# 3) Dodaj else po pętli while z tekstem w konsoli "Koniec pętli while"
# 4) Zapisz podsumowanie "Suma wartości:" oraz wynik sumy

i = 0
sum = 0

while i <= 100:
    sum += i
    i += 1
else:
    print("Koniec pętli while.")

print("Suma liczb od 0 do 100: " + str(sum))
