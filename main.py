import discord
import os

TOKEN = os.getenv('TOKEN')

class Bot(discord.client):
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to discord')


client.run(TOKEN, intents=discord.Intents.default())