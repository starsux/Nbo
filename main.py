import discord
import os
print(os.getenv('TOKEN'))
TOKEN = os.getenv('TOKEN')
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')

client.run(TOKEN)