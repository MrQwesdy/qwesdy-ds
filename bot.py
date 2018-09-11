import discord
from discord.ext import commands
import asyncio
import aiohttp

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

TOKEN = 'NDg4MjM2NDQ0MjY4MjMyNzE2.Dngjqw.bPKFYK26L-UVOrzwLFKxZRok5rw'

minutes = 0
hour = 0

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='.help | By Qwesdy',type=3))
    print('Connected')

# Testing

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number=500):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await client.delete_message(x)
            counter += 1

@client.command(pass_context=True)
async def help(ctx):
    channel = ctx.message.channel
    embed = discord.Embed (
        title = '__**Command List**__',
        description = '** **',
        colour = discord.Colour.blue()
    )

    embed.add_field(name=".help", value="Information about bot", inline=False)
    embed.add_field(name=".uptime", value="Shows you uptime of Bot", inline=False)
    embed.add_field(name=".invite", value="Invite Link to Our Discord", inline=False)
    embed.add_field(name=".ig", value="Qwesdy's Instagram", inline=False)
    embed.add_field(name=".qwenty", value="Qwenty's Discord", inline=False)
    embed.add_field(name=".dev", value="Bot Developer", inline=False)
    embed.add_field(name=".add", value="Add this bot to your own Server", inline=False)

    await client.send_message(channel, embed=embed)

# Admin

@client.command(pass_context=True)
async def admin(ctx):
    channel = ctx.message.channel
    embed = discord.Embed (
        title = '__**Admin Commands**__',
        description = '** **',
        colour = discord.Colour.blue()
    )

    embed.add_field(name=".clear", value="Delete all messages in channel", inline=False)
    embed.add_field(name=".kick", value="Kick user from Discord", inline=False)

    await client.send_message(channel, embed=embed)

# Admin

@client.command()
async def invite():
    await client.say("Invite link » `https://discord.gg/gHq5uW5`")

@client.command()
async def ig():
    await client.say("Qwesdy's IG » `@Qwesdy_`")

@client.command()
async def qwenty():
    await client.say("Qwenty's Discord » `https://discord.gg/gmh8ay`")

@client.command()
async def dev():
    await client.say("Bot Developer » `Qwesdy`")
    
@client.command()
async def add():
    await client.say("Link » `https://discordapp.com/oauth2/authorize?client_id=488236444268232716&permissions=8&scope=bot`")


async def msg():
    await client.say('Test Message')

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await client.say(" {} has been kicked".format(user.mention))
    await client.kick(user)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Neighbor')
    await client.add_roles(member, role)


client.run(TOKEN)
