import discord
from discord.ext import commands, tasks

from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv('.env')
client = commands.Bot(command_prefix = '/')
dt = datetime.now().strftime('%m/%d/%Y - %H:%M:%S')


@client.event
async def on_connect():
    print('~~~~~~~~~~~~')
    print(f'[{dt}] Logged in as {client.user.name} (ID: {client.user.id})')

@client.event
async def on_resume():
    print(f'[{dt}] Reconnected!')

@client.event
async def on_ready():
    try:
        print('Discord.py Version: {}'.format(discord.__version__))
        print(f'{client.user.name} is ready.')
        client.load_extension('cogs.messenger')
        client.load_extension('cogs.translate')
    except Exception as e:
        print(e)
        
@client.event
async def on_disconnect():
   print(f'[{dt}] Reconnected!')

client.run(os.getenv('TOKEN'))