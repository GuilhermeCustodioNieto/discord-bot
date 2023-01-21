import discord
import funcoes_discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswich('$d6'):
        await message.channel.send(funcoes_discord.d6())

client.run('MTAwMzg1Nzc2NDc3MjIxNjg4Mg.GHAOGb.KhiYvc2OM7G1nEqHFQtaeeUJ4-xYg3D0fx2vTc')