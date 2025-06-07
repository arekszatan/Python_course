
text = "Hello world!"
print(text)
print(len(text)) # number of char
print(type(text)) # type of variable

print(text[len(text) - 1])

print(text[0:5]) # Hello

print(text * 4)
strX3 = text * 3
print(strX3)

str2 = text + " and Hello again!"
print(str2)

print(str2[6:])

print(str2[::3]) # wyswietlanie co którąś litere

multiLine = """Pierwsza linia,
druga linia,
trzecia linia
"""

print(multiLine)

multiLine2 = "Pierwsza linia\ndruga linia\ntrzecia\t linia\""
print(multiLine2)
