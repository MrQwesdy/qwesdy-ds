import discord, datetime, time
from discord.ext import commands
import asyncio
import aiohttp
import os
import json
import random

extensions = ['blacklist', 'uptime', 'test1']

client = commands.Bot(command_prefix = '.')
client.remove_command('help')
TOKEN = 'NTEyNjQxNDk5Nzc1NjMxMzc5.Ds8aOg.MdfgLphrylJQslYfYeKi3nQtaqg'

minutes = 0
hour = 0

players = {}

# Startup

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='.help',type=2))
    print('Connected')
    print('Developed by Qwesdy')
    print(' ')

# Reaction

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '🐧':
        print('qwesdy g0d')

# Userinfo Cmd

@client.command(pass_context=True)
async def info(ctx, user: discord.Member):

    # Then we start getting the actual data and run that smoothly into our embed, we use the code below as a simple framework

  embed = discord.Embed(title="User Information", description='', color=ctx.message.author.color)
  embed.add_field(name='Name', value='{}'.format(user.name))
  embed.add_field(name='ID', value='{}'.format(user.id), inline=True)
  embed.add_field(name='Status', value='{}'.format(user.status), inline=True)
  embed.add_field(name='Highest Role', value='<@&{}>'.format(user.top_role.id), inline=True)
  embed.add_field(name='Joined at', value='{:%d/%h/%y at %H:%M}'.format(user.joined_at), inline=True)
  embed.add_field(name='Created at', value='{:%d/%h/%y at %H:%M}'.format(user.created_at), inline=True)
  embed.add_field(name='Discriminator', value='{}'.format(user.discriminator), inline=True)
  embed.add_field(name='Playing', value='{}'.format(user.game))
  embed.set_footer(text="Developed by Qwesdy", icon_url='{}'.format(user.avatar_url))
  embed.set_thumbnail(url=user.avatar_url)

  await client.say(embed=embed)

# Load Cmd

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        await client.send_message(message.channel, '{} loaded successfully'.format(extension))
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))

# Unload Cmd

@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded. [{}]'.format(extension, error))


if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

# Help Cmd

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Commands:", description="", colour=ctx.message.author.top_role.colour)
    embed.add_field(name="** **", value="** **", inline=False)
    embed.add_field(name=".clear (amount) - Clears the chosen amount of messages in current channel.", value="** **", inline=False)
    embed.add_field(name=".mute (@User) - Gives Mute role to an chosen User.", value="** **", inline=False)
    embed.add_field(name=".unmute (@User) - Unmutes already muted chosen User.", value="** **", inline=False)
    embed.add_field(name=".kick (@User) - Kicks chosen User from the Server.", value="** **", inline=False)
    embed.add_field(name=".ban (@User) - Permanently IP Bans an chosen User from the server", value="** **", inline=False)
    embed.add_field(name="To unban someone you have to do it manualy through Server Settings!", value="** **", inline=False)
    embed.add_field(name="** **", value="** **", inline=False)
    embed.add_field(name="Found by Qwenty.#7942", value="** **", inline=False)
    embed.add_field(name="Developed by Qwesdy#9217", value="** **", inline=False)
    embed.add_field(name="** **", value="** **", inline=False)
    embed.add_field(name="Made with :heart:", value="** **", inline=False)
    await client.say(embed=embed)

# Clear Cmd

@client.command(pass_context = True)
async def clear(ctx, amount=100):
    if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == '194151340090327041':
        channel = ctx.message.channel
        messages = []
        async for message in client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await client.delete_messages(messages)
        bagr = await client.say('Messages deleted' + ' ' + '(' + str(amount) + ')')
        await asyncio.sleep(3)

        await client.delete_message(bagr)

# Ban Cmd

@client.command(pass_context = True)
async def ban(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == '194151340090327041':
        embed=discord.Embed(title="Ban Command", description="**{0}** has been banned!".format(user, ctx.message.author), color=ctx.message.author.top_role.colour)
        await client.say(embed=embed)
        await client.ban(user)

# Kick Cmd

@client.command(pass_context = True)
async def kick(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == '194151340090327041':
        embed=discord.Embed(title="Kick Command", description="**{0}** has been kicked!".format(user, ctx.message.author), color=ctx.message.author.top_role.colour)
        await client.say(embed=embed)
        await client.kick(user)

# Mute Cmd

@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="Mute Command", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=ctx.message.author.top_role.colour)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

# Unmute Cmd

@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="Unmute Command", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=ctx.message.author.top_role.colour)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

# Auto role

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Not Verified')
    await client.add_roles(member, role)
    await client.send_message(member, "Welcome on the Qwesdy's Development Discord\n\nPlease Verify in First Channel (verify)\n\nIf you have any questions DM me. (Qwesdy#9217)")

client.run(TOKEN)
