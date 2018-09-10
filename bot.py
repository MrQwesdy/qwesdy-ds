import discord
from discord.ext import commands
import asyncio
import aiohttp

TOKEN = 'NDg4MjM2NDQ0MjY4MjMyNzE2.DnaHWA.Hv2eXu36OBnWowxe3F-IvuILnKY'

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

minutes = 0
hour = 0

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='.help | By Qwesdy',type=3))
    print('Connected')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

# Testing



@client.event
async def on_message(message):
    if message.content.startswith('.help'):
        embed = discord.Embed(title="__**Command List**__", description="", color=0x00ff00)
        embed.add_field(name=".help", value="Information about bot", inline=False)
        embed.add_field(name=".uptime", value="Shows you uptime of Bot", inline=False)
        embed.add_field(name=".invite", value="Invite Link to Our Discord", inline=False)
        embed.add_field(name=".ig", value="Qwesdy's Instagram", inline=False)
        embed.add_field(name=".qwenty", value="Qwenty's Discord", inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('.uptime'):
        embed = discord.Embed(title="__**Uptime**__", description="", color=0x00ff00)
        embed.add_field(name="Hours", value="{0}".format(hour, minutes, message.server), inline=False)
        embed.add_field(name="Minutes", value="{1}".format(hour, minutes, message.server), inline=False)
        embed.add_field(name="** **", value="** **", inline=False)
        embed.add_field(name="in", value="{2}".format(hour, minutes, message.server), inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('.invite'):
        await client.send_message(message.channel, "Invite link » `https://discord.gg/gHq5uW5`")

    if message.content.startswith('.ig'):
        await client.send_message(message.channel, "Qwesdy's IG » `@Qwesdy_`")

    if message.content.startswith('.qwenty'):
        await client.send_message(message.channel, "Qwenty's Discord » `https://discord.gg/gmh8ay`")

    if message.content.startswith('.dev'):
        await client.send_message(message.channel, "Bot Developed by `Qwesdy`")

# Testing

async def uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Neighbor')
    await client.add_roles(member, role)

@client.command()
async def msg():
    embed = discord.Embed(
        title = 'Information',
        description = '',
        colour = discord.Colour.red()
    )
    embed.set_image(url='https://cdn.discordapp.com/attachments/486513293238730763/487250206358896640/rainbow_line_gif.gif')
    embed.add_field(name='ahojky', value='ahojky', inline=False)

    await client.say(embed=embed)

client.loop.create_task(uptime())
client.run(TOKEN)
