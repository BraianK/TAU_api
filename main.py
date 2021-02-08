import requests
import json

coin = 'btc-bitcoin'
url = "https://api.coinpaprika.com/v1/coins/{}".format(coin)
head = {'content-type': 'application/json'}
response = requests.request("GET", url)
a = json.loads(response.text)

print(a)