import discord
import os

TOKEN = os.getenv('TOKEN')

class BotClient(discord.Client):
    @client.event
    async def on_ready():
        print(f'{client.user} has connected to discord')


intents = discord.Intents.default()
client = BotClient(intents=intents)
client.run(TOKEN)