import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook
from mcstatus import JavaServer
import requests
import json
import time
from datetime import datetime

mc_server_url = " YOUR DISCORD WEB HOOK HERE "

# multithreading mc server status check
def update_mc():
    while True:
        try:
            # MAKE SURE TO EDIT THE IP TO YOUR MC SERVER \/
            server = JavaServer.lookup("135.148.145.141:25584")
            status = server.status()
            latency = round(server.ping(), 2)
            
            webhook = DiscordWebhook(url=mc_server_url, content=f"""
```yaml
Rubiix's Minecraft Server!
``````
135.148.145.141:25584
``````css
[Version 1.18.2]
``````yaml
[Players Online: {status.players.online}]
[Latency: {latency}ms]
```
            """)
            sent_webhook = webhook.execute()
            print(f"Sending mc webhook... [{datetime.now()}]")
            time.sleep(60)
            webhook.delete(sent_webhook)
            
        except Exception as e:
            print("MC webhook failed. (Server offline) [{datetime.now()}]")
            webhook1 = DiscordWebhook(url=mc_server_url, content=f"""
```yaml
Rubiix's Minecraft Server!
``````
135.148.145.141:25584
``````css
[Version 1.18.2]
``````css
[Server Offline]
```
            """)
            sent_webhook1 = webhook1.execute()
            time.sleep(60)
            webhook1.delete(sent_webhook1)

update_mc()