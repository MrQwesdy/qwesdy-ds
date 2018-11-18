import discord
from discord.ext import commands
import checks
import asyncio

class test1():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_owner()
    @commands.command(name='test1', pass_context=True)
    async def choice(self, ctx):
        '''test1'''
        await self.bot.delete_message(ctx.message)

        msg = await self.bot.say('Po kliknutí na emoji dostaneš roli.')
        await self.bot.add_reaction(msg, '\U00002705')

        await asyncio.sleep(0.1)
        while True:
            res = await self.bot.wait_for_reaction(['\U00002705', '\U0000274C'], message=msg)
            if res.reaction.emoji == '\U00002705':
                await self.bot.add_roles(res.user, discord.utils.get(msg.server.roles, name='Member'))
                await self.bot.remove_roles(res.user, discord.utils.get(msg.server.roles, name='Not Verified'))


def setup(bot):
    bot.add_cog(test1(bot))
