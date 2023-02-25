import discord


TOKEN = "MTA3ODQxNjYxMTM2NDU2OTExOA.GoI6Eg.uqTRGZahXOuAM6xPvAopwikuzeVN78dAm2wUM8"
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')

client.run(TOKEN)