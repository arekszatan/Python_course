# pip install requests
import requests_1

def fetch_exchange_rates():
    """
    Funkcja do pobierania i wyświetlania kursów walut z API NBP
    """
    url = "http://api.nbp.pl/api/exchangerates/tables/a/?format=json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("Otrzymano kursy walut:")
        for rate in data[0]['rates']:
            print(f'{rate['currenct']}: {rate['code']} = {rate['mid']}')
    except Exception as e:
        print(f'Wystąpił błąd {e}')

if __name__ == '__main__':
    fetch_exchange_rates()


def post(url, data):
    return None