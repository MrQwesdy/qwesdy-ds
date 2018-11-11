import discord, datetime, time
from discord.ext import commands
import asyncio
import aiohttp
import os
import random

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

TOKEN = 'NDg4MjM2NDQ0MjY4MjMyNzE2.DshKfQ.WtBtaxlbLXs-M2IC01jWfLhM5aw'

minutes = 0
hour = 0

players = {}

# Startup

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    await client.change_presence(game=discord.Game(name='.help | By Qwesdy',type=3))
    print('Connected')

# Send Shop Message

async def status_task():
    while True:
        await client.send_message(client.get_channel('495608748488785933'), 'Qwentyho Shop » https://selly.gg/@Qwenty__')
        await asyncio.sleep(1800)
        await client.send_message(client.get_channel('495608748488785933'), 'Qwentyho Shop » https://selly.gg/@Qwenty__')
        await asyncio.sleep(1800)

# Clear Cmd

@client.command(pass_context = True)
async def clear(ctx, number=50000):
    if ctx.message.author.server_permissions.ban_members or ctx.message.author.id == '194151340090327041':
        channel = ctx.message.channel
        messages = []
        channel = ctx.message.channel
        bagr = 1
        async for message in client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await client.delete_messages(messages)
        await client.say('Messages deleted')
        await asyncio.sleep(3)
        async for bagr in client.logs_from(channel, limit=int(amount) + 1):
            messages.append(bagr)
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
        role = discord.utils.get(member.server.roles, name='Mute')
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
        role = discord.utils.get(member.server.roles, name='Mute')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="Unmute Command", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=ctx.message.author.top_role.colour)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)


# Auto role

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member, role)

client.run(TOKEN)
