import discord
import os

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')

@client.event
async def on_message(msg):
    # To avoid bot message
    if(msg.author == client.user): return

    if(msg.content.startswith(comand_char + "/help")):
        await msg.channel.send("No")

client.run(TOKEN)