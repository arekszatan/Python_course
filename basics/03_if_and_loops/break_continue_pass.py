
data = [0, 1, 2, 3, 4, 5]

for i in data:
    if i == 3:
        break
    print(i * 2)

print("")

for i in data:
    if i == 3 or i == 5:
        continue
    print(i)

print("")

if 30 > 20:
    pass # pusty wypełniacz, nic nie robi
else:
    pass
