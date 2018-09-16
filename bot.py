import discord, datetime, time
from discord.ext import commands
import asyncio
import aiohttp
import os
import random

start_time = time.time()

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

TOKEN = 'NDg4MjM2NDQ0MjY4MjMyNzE2.Dngjqw.bPKFYK26L-UVOrzwLFKxZRok5rw'

minutes = 0
hour = 0

players = {}

@client.event
async def on_ready():
    client.add_cog(Uptime(client))
    await client.change_presence(game=discord.Game(name='.help | By Qwesdy',type=3))
    print('Connected')

# Uptime Cmd

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

# Clear Cmd

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number=50000):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in client.logs_from(ctx.message.channel, limit = number):
        await client.delete_message(x)

# News Cmd

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

# Help Cmd

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="__**List of Player Commands**__", description="", colour=ctx.message.author.top_role.colour)
    embed.add_field(name=".help", value="Information about bot", inline=False)
    embed.add_field(name=".fun", value="Fun Commands", inline=False)
    embed.add_field(name=".admin", value="Commands for Admin", inline=False)
    embed.add_field(name=".uptime", value="Shows you uptime of Bot", inline=False)
    embed.add_field(name=".invite", value="Invite Link to Our Discord", inline=False)
    embed.add_field(name=".ig", value="Qwesdy's Instagram", inline=False)
    embed.add_field(name=".qwenty", value="Qwenty's Discord", inline=False)
    embed.add_field(name=".dev", value="Bot Developer", inline=False)
    embed.add_field(name=".add", value="Add this bot to your own Server", inline=False)
    await client.say(embed=embed)

# Admin Cmd

@client.command(pass_context=True)
async def admin(ctx):
    embed = discord.Embed(title="__**List of Admin Commands**__", description="", colour=ctx.message.author.top_role.colour)
    embed.add_field(name=".clear", value="Delete all messages in channel", inline=False)
    embed.add_field(name=".ban", value="Ban user from Discord", inline=False)
    embed.add_field(name=".kick", value="Kick user from Discord", inline=False)
    embed.add_field(name=".mute", value="Mute user on Discord", inline=False)
    await client.say(embed=embed)

# Fun Cmd

@client.command(pass_context=True)
async def fun(ctx):
    embed = discord.Embed(title="__**List of Fun Commands**__", description="", colour=ctx.message.author.top_role.colour)
    embed.add_field(name=".bite", value="You can bite your friend", inline=False)
    await client.say(embed=embed)

# Invite Cmd

@client.command()
async def invite():
    await client.say("Invite link » `https://discord.gg/BU3vA28`")

# Instagram Cmd

@client.command()
async def ig():
    await client.say("Qwesdy's IG » `@Qwesdy_`")

# Qwenty Cmd

@client.command()
async def qwenty():
    await client.say("Qwenty's Discord » `https://discordapp.com/invite/cFEfmNh`")

# Dev Cmd

@client.command()
async def dev():
    await client.say("Bot Developer » `Qwesdy`")
    
# Add Cmd

@client.command()
async def add():
    await client.say("Link » `https://discordapp.com/oauth2/authorize?client_id=488236444268232716&permissions=8&scope=bot`")

# Test Cmd

async def msg():
    await client.say('Test Message')

# Ban Cmd

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
        role = discord.utils.get(member.server.roles, name='Mute')
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

# Join Voice Channel Cmd

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def join(ctx):
   author = ctx.message.author
   voice_channel = author.voice_channel
   vc = await client.join_voice_channel(voice_channel)

# Leave Voice Channel Cmd

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def leave(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

# Play Music Cmd

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def yt(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

# Bite Cmd

@client.command(pass_context=True)
async def bite(ctx, member: discord.Member):
    channel = ctx.message.channel

    imgList = os.listdir("./bite_img") # Creates a list of filenames from your folder

    imgString = random.choice(imgList) # Selects a random element from the list

    path = "./bite_img/" + imgString # Creates a string for the path to the file

    await client.send_message(channel, ":speech_balloon: {0} you have been bitten by {1} :speech_balloon:".format(member.mention, ctx.message.author.mention))
    await client.send_file(channel, path) # Sends the image in the channel the command was used


# Random Image Cmd

@client.command(pass_context=True)
async def bagr(ctx):
    channel = client.get_channel("490255926700277773")
    messages = ["Hello!", "How are you doing?", "Howdy!"]
    await client.send_message(channel, random.choice(messages))
    await asyncio.sleep(120)

# Other Cmds

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member, role)

client.run(TOKEN)
