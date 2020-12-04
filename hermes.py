import discord
from discord.ext import commands, tasks

from dotenv import load_dotenv
import os
import math


load_dotenv('.env')
client = commands.Bot(command_prefix = '/')

class Messenger(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None
    
    @commands.command()
    async def hello(self, ctx,*args, member: discord.Member=None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello, {0.name}'.format(member))
        else:
            await ctx.send('Hello, {0.name}. Nice to see you.'.format(member))
        self._last_member = member


@client.event
async def on_ready():
    try:
        print('Discord.py Version: {}'.format(discord.__version__))
        print(f'{client.user.name} is ready.')
    except Exception as e:
        print(e)
        

@client.command()
async def ping(message):
    await message.send(f'Latency: {math.trunc(client.latency * 1000)}ms')

client.add_cog(Messenger(client))
client.run(os.getenv('TOKEN'))