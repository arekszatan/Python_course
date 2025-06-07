
setData = {2, 3, 1, 4, 5}
setData.add(22)
setData.discard(2)
print(type(setData)) # <class 'set'>
print(setData)

for v in setData:
    print(v)

frozenData = frozenset(setData)
print(type(frozenData))

#frozenData.add(10)

for value in frozenData:
    print(value)