import discord
from discord.ext import commands

import math

class Messenger(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    @commands.command(aliases=['hello','hi','howdy'])
    async def greetings(self, ctx, *args, member: discord.Member=None):
        member = member or ctx.author
        e = discord.Embed(description='foo')
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello, {0.name}'.format(member), embed=e)
        else:
            await ctx.send('Hey, {0.name}.'.format(member), embed=e)
        self._last_member = member

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Latency: {math.trunc(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Messenger(client))