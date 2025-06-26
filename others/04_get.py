import requests
import json

url = 'https://httpbin.org/get'

params = {
    'username' : 'nowy_użytkownik',
    'page' : 5
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Otrzymane dane")
    formatted_json = json.dumps(response.json(), indent=4)
    print(formatted_json)
else:
    print(f'Błąd zapytania: {response.status_code}')