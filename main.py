import discord
import os

TOKEN = os.getenv('TOKEN')

class BotClient(discord.Client):
    client = self
    command_char = "/"
    async def on_ready():
        print(f'{client.user} has connected to discord')

    async def on_message(msg):
        # To avoid bot message
        if(msg.author == client.user): return

        if(msg.content.startswith(comand_char + "help")):
            await msg.channel.send("No")


intents = discord.Intents.default()
client = BotClient(intents=intents)
client.run(TOKEN)