
for v in [1, 2, 3, 4]:
    print(v * 2)

for v in ("Ania", "Ola", "Rafał"):
    print(v)

for el in {3, 4, 5, 6, "Ola"}:
    print(el)

for v in "Hello":
    print(v)
else:
    print("Pętla zakończona.")

dictionary_data = {
    "Ania" : "ania@example.com",
    "Adam" : "adam@example.com"
}

for key in dictionary_data:
    print(key)

for key in dictionary_data.keys():
    print(key)

for value in dictionary_data.values():
    print(value)

for key, value in dictionary_data.items():
    print(key + " : " + value)

