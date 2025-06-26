import requests
import json

# Definiowanie adresu URL endpointu, do którego będziemy wysyłać zapytanie POST
url = 'https://httpbin.org/post'

data = {
    'username' : "Ania",
    'password' : 'sd#$TggDFG',
    'email' : 'ania@example.com',
    'date_of_birth' : '2000-01-01',
    'country' : 'Polska'
}

response = requests.post(url,data=data)

if response.status_code == 200:
    response_data = response.json()
    print("Odpowiedź z serwera!")

    print(json.dumps(response_data, indent=4))
else:
    print(f'Nie udało się wysłać danych, kod statusu {response.status_code}')