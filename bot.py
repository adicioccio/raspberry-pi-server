import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook
from mcstatus import JavaServer
import requests
import json
import time


# create new discord client / bot
client = discord.Client()
token = "OTgzNDcwNTcwMzEyMTgzODQy.G2Wzoe.MpRz43DQoiIfqTlxYU7awRlQnGmPEp98EC-764"
admin = "Rubiix#2160"


# display message when bot is online
@client.event
async def on_ready():
    print("{0.user} is now Online.".format(client))


# bot commands
@client.event
async def on_message(message):
    # return nothing if bot called command itself
    if message.author == client.user:
        return

    # simple ping pong
    if message.content.startswith("-ping") and str(message.channel.name) == "bot-commands":
        await message.channel.send("pong!")

    # admin commands
    if message.content.startswith("-a"):
        if str(message.author) == admin:
            output = message.content
            sliced = output[2:]
            await message.channel.send(sliced)
        else:
            await message.channel.send("```You don't have access to this command!```")


# run the bot using secret token address
client.run(token)

