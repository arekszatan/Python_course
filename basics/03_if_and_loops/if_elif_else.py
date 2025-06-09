
num = 5

# 3 spacje za dwukrpokiem po if jako wcięcie również działają
if num >= 3:
    print("num jest większa lub równa 3")
    print("oraz !")

if num == 5:
    print("5 == 5")

num = 20

if num == 1:
    print("num == 1")
elif num == 2:
    print("num == 2")
elif num == 5:
    print("num == 5")
elif num == 10:
    print("num == 10")
elif num >= 11:
    print("num >= 11")
else:
    print("domyśly kod jeśli reszta porównań da false")

print("Dalszy kod")

if 5 > 1: print("5 > 1")

if 10 > 2:
    print("10 > 2")
    if 4 > 1:
        print("4 > 1")
        if 3 > 2:
            print("3 > 2")
        print("4 > 1 ciąg dalszy")


