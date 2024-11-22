import requests


response = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=11")
exchange_json = response.json()

usd_exchenge = [exchange_dict for exchange_dict in exchange_json if exchange_dict.get("ccy") == "USD"][0]

print(usd_exchange.get("buy"))
