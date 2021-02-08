import requests
import json
#link do api https://api.coinpaprika.com/#tag/Coins/paths/~1coins/get
coin = 'btc-bitcoin'
url = "https://api.coinpaprika.com/v1/coins/{}".format(coin)
head = {'content-type': 'application/json'}
response = requests.request("GET", url)
a = json.loads(response.text)
#Wyświetlenie items
print(a.items())
# -----------------------------------
# sprawdzanie kluczy
expected = ['id', 'name', 'symbol', 'rank']
current = []

for key, value in a.items():
    if key in expected:
        current.append(key)
assert expected == current
#Wyświetlenie wartości oczekiwanej i aktualnej
print(expected)
print(current)
# -----------------------------------
# sprawdzanie odpowiedzi
assert response.status_code == 200
#Wyświetlenie odpowiedzi
print(response.status_code)
# -----------------------------------
# sprawdzanie niepoprawnego zapytania
url = "https://api.coinpaprika.com/v1/acoins/{}".format(coin)  # zmiana endpointu z cases na a
response = requests.request("GET", url)
assert response.status_code == 404
#Wyświetlenie odpowiedzi
print(response.status_code)