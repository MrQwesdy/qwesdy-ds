import discord
import asyncio
from discord.ext import commands

class Blacklist:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot: return
        if 'kokot' in message.content:
            await self.client.delete_message(message)
            await self.client.send_message(message.author, "Keyword `kokot` is not allowed on Qwesdy's Server")
            await self.client.send_message(message.channel, "That keyword is not allowed here")

def setup(client):
    client.add_cog(Blacklist(client))
