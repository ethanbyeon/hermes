import discord
from discord.ext import commands

from googletrans import Translator

class Translate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def translate(self, ctx, language, *message):
        translator = Translator()
        translations = translator.translate(list(message), dest=language)
        await ctx.send([print(translation.origin, ' -> ', 'translation.text') for translation in translations])

def setup(client):
    client.add_cog(Translate(client))