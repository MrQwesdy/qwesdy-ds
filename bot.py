import discord, datetime, time
from discord.ext import commands
import asyncio
import aiohttp

start_time = time.time()

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

TOKEN = 'NDg4MjM2NDQ0MjY4MjMyNzE2.Dngjqw.bPKFYK26L-UVOrzwLFKxZRok5rw'

minutes = 0
hour = 0

@client.event
async def on_ready():
    client.add_cog(Uptime(client))
    await client.change_presence(game=discord.Game(name='.help | By Qwesdy',type=3))
    print('Connected')


class Uptime:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Developed by Qwesdy")
        try:
            await self.bot.say(embed=embed)
        except discord.HTTPException:
            await self.bot.say("Current uptime: " + text)




# Testing

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number=50000):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit = number):
        await client.delete_message(x)

@client.command(pass_context=True)
async def news(ctx):
    channel = ctx.message.channel
    embed = discord.Embed (
        title = '__**Command List**__',
        description = '** **',
    )
    embed = discord.Embed(colour=ctx.message.author.top_role.colour)
    embed.add_field(name="Update v1.0", value="** **", inline=False)
    embed.add_field(name="• Added .ban", value="** **", inline=False)
    embed.add_field(name="• Added .mute", value="** **", inline=False)
    embed.add_field(name="• Added .kick", value="** **", inline=False)

    await client.send_message(channel, embed=embed)


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="__**List of Player Commands**__", description="", colour=ctx.message.author.top_role.colour)
    embed.add_field(name=".help", value="Information about bot", inline=False)
    embed.add_field(name=".admin", value="Commands for Admin", inline=False)
    embed.add_field(name=".uptime", value="Shows you uptime of Bot", inline=False)
    embed.add_field(name=".invite", value="Invite Link to Our Discord", inline=False)
    embed.add_field(name=".ig", value="Qwesdy's Instagram", inline=False)
    embed.add_field(name=".qwenty", value="Qwenty's Discord", inline=False)
    embed.add_field(name=".dev", value="Bot Developer", inline=False)
    embed.add_field(name=".add", value="Add this bot to your own Server", inline=False)
    await client.say(embed=embed)

# Admin

@client.command(pass_context=True)
async def admin(ctx):
    embed = discord.Embed(title="__**List of Admin Commands**__", description="", colour=ctx.message.author.top_role.colour)
    embed.add_field(name=".clear", value="Delete all messages in channel", inline=False)
    embed.add_field(name=".ban", value="Ban user from Discord", inline=False)
    embed.add_field(name=".kick", value="Kick user from Discord", inline=False)
    embed.add_field(name=".mute", value="Mute user on Discord", inline=False)
    await client.say(embed=embed)

# Admin

@client.command()
async def invite():
    await client.say("Invite link » `https://discord.gg/gHq5uW5`")

@client.command()
async def ig():
    await client.say("Qwesdy's IG » `@Qwesdy_`")

@client.command()
async def qwenty():
    await client.say("Qwenty's Discord » `https://discordapp.com/invite/cFEfmNh`")

@client.command()
async def dev():
    await client.say("Bot Developer » `Qwesdy`")
    
@client.command()
async def add():
    await client.say("Link » `https://discordapp.com/oauth2/authorize?client_id=488236444268232716&permissions=8&scope=bot`")


async def msg():
    await client.say('Test Message')

@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
    embed=discord.Embed(title="Ban Command", description="**{0}** has been banned!".format(user, ctx.message.author), color=ctx.message.author.top_role.colour)
    await client.say(embed=embed)
    await client.ban(user)

# Mute Cmd

@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="Mute Command", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=ctx.message.author.top_role.colour)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

# Kick Cmd

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    embed=discord.Embed(title="Kick Command", description="**{0}** has been kicked!".format(user, ctx.message.author), color=ctx.message.author.top_role.colour)
    await client.say(embed=embed)
    await client.kick(user)

# Other

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Neighbor')
    await client.add_roles(member, role)


client.run(TOKEN)
