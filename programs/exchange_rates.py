import requests

response = requests.get('https://google.com')

if response.ok:
    data = response.json()
    rates = data["rates"]
    base = data["base"]
    date = data["date"]

print("base: " + base)
print("date: " + date)

for key in rates:
    print(key + ": ", rates[key])