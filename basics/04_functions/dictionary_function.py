
data = {"name" : "Ola", "city" : "Waw"}
print(data["name"])
data_postal_code = "postal_code"
data[data_postal_code] = 12345
print(data)
print(len(data))

del data["city"]
print(data)
data.clear()
print(data)

data = {"name": "Kasia", "city": "Krk"}
data_copy = data.copy()
print(data_copy)
print(data["name"] is data_copy["name"]) # True
print(data is data_copy) # False

data2 = dict.fromkeys(("name", "city", "code"))
print(data2)

data3 = dict.fromkeys(("name", "city", "code"), 0)
print(data3)

print(data2.get("x", "DEFAULT"))
print(data2.get("name", "DEFAULT"))

print("name" in data2)
print("x" in data2)

print(data2.keys())
print(data2.values())