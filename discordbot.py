import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
guild = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()
client = discord.Client(command_prefix=',', intents=intents)

@client.event 
async def on_ready():
        print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "vxtwitter.com" in message.content:
         return
    if "twitter.com" in message.content:
        new_message = message.content.replace("twitter.com", "vxtwitter.com")
        await message.channel.send(f"Here's the modified link: {new_message}")
    if "vxtiktok.com" in message.content:
         return
    if "tiktok.com" in message.content:
        new_tiktok = message.content.replace("tiktok.com", "vxtiktok.com")
        await message.channel.send(f"Here's the modified link: {new_tiktok}")
    if "ddinstagram.com" in message.content:
         return
    if "instagram.com" in message.content:
        new_ig = message.content.replace("instagram.com", "ddinstragram.com")
        await message.channel.send(f"Here's the modified link: {new_ig}") 

client.run(token)