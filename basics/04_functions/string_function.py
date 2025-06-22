print("Hello " + "World")
print("Hello " * 3)

string = "Hello World!"
print(string[0]) # H
print(string[0:5]) # Hello

print("Hello" in string) # True
print("Hello" not in string) # False

multiline = """line 1
line 2
line 3
"""

print("ala".capitalize())
print("Ola ma kota. Ola ma psa".count("Ola"))

print("Hello".center(30, "$"))

print(string.startswith("Hello"))
print(string.endswith("World!"))

print(string.find("Ola"))
print(string.find("llo"))

print("Ola ma kota. Ola ma psa".rfind("Ola"))

print("132443242".isalnum())
print("132443242.".isalnum())
print("132443242k".isalnum())

print("341241241".isalpha())
print("kot".isalpha())
print("kot ".isalpha())
print("kot2".isalpha())

print("test".islower())
print("tesT".islower())

print("TEST".isupper())

print(" \n \t ".isspace())
print(" \n \tw ".isspace())

print("-|".join(["Ala", "Ola", "Adam"]))

print("Hello World!".lower())
print("Hello World!".upper())
print("Hello World!".swapcase())

print("   \n \t    Hello World!  \n \t".lstrip())
print("   \n \t    Hello World!  \n \t".rstrip())
print("   \n \t    Hello World!  \n \t".strip())

print("Ola ma psa. Ola ma kota.".replace("Ola", "Kasia"))

print("My name is {myName}, I am from {country}".format(myName = "Kuba", country = "Poland"))
print("My name is {myName}, my postal code is {code}".format(myName = "Kuba", code = 123132))
print("My name is {0}, my postal code is {1}".format("Kuba", 123132))

