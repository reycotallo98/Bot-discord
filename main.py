
import os
import discord
from discord import *
import g4f
import asyncio
intents = discord.Intents.default()
intents.message_content = True
intents.auto_moderation = True
intents.bans = True
intents.messages = True
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
    try:
        if str(message.content).index('porn') > -1 or str(message.content).index('xvideos') > -1:
            await message.channel.send('/kick ' + message.author.mention)
    except:
        pass
    if message.channel.name == "ideas":
      result = g4f.ChatCompletion.create_async(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ("Un usuario necesita ayuda para empezar en ciberseguridad, nos ha mandado este mensaje " + str(message.content) + " . Por favor dale consejo teniendo en cuenta que contamos con numerosos grupos de estudio entre ellos criptografía, seguridad de redes, seguridad web, ingenieria social, forense digital, seguridad movil. Además anímale a estar activo en la comunidad, compartir sus avances e investigaciones con nosotros, la comunidad se llama b1tBusters")}])
      
      await message.channel.send(await result)
my_secret = os.environ['discordToken']
client.run(my_secret)