import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook
from mcstatus import JavaServer
import requests
import json
import time
from datetime import datetime

crypto_prices_url = " YOUR DISCORD WEB HOOK HERE "
coingecko_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad"

def update_crypto():
    while True:
        try:
            request = requests.get(url=coingecko_url)
            data = request.json()
            webhook = DiscordWebhook(url=crypto_prices_url, content=f"""
```html
Bitcoin  [BTC]: {data[0]['current_price']} CAD
Ethereum [ETH]: {data[1]['current_price']} CAD
```
""")
            sent_webhook = webhook.execute()
            print(f"Sending crypto webhook... [{datetime.now()}]")
            time.sleep(120)
            webhook.delete(sent_webhook)
        except Exception as e:
            print(f"Crypto webhook failed. ({e}) [{datetime.now()}]")

update_crypto()