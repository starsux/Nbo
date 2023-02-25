import discord
import os

TOKEN = os.getenv('TOKEN')

class BotClient(discord.Client):
    @client.event
    async def on_ready():
        print(f'{self.user} has connected to discord')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)