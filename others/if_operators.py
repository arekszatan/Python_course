
num = 12
if num > 5:
    print(str(num) + " większe od 5")
    # instrukcje if można zagnieżdżać
    if num >= 10:
        print(str(num) + " większe też od 10")
        if num > 20:
            print(str(num) + " większe też od 20")
    print("Ostatnie wcięcie instrukcji if")

print("Informacja nie zależna od bloku kodu if")

num = 7
if num == 7:
    print("num jest 7")
elif num == 10:
    print("num jest 10")

a = 10
b = 5

if a == b:
    print("a równe b")
elif a < b:
    print("a < b")
else:
    print("a > b")

# warto również wspomnieć, że można zapisać
# w jednej linijce kod do wyponania po if
if a > b: print("a jest większe od b")