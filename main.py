import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv('.env')
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('HERMES is ready.')

client.run(os.getenv('TOKEN'))