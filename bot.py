import discord, datetime, time
from discord.ext import commands
import asyncio
import aiohttp
import os
import random
import youtube_dl
import requests as rq

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

TOKEN = 'NDg4MjM2NDQ0MjY4MjMyNzE2.DshKfQ.WtBtaxlbLXs-M2IC01jWfLhM5aw'

minutes = 0
hour = 0

players = {}

from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

# Startup

@client.event
async def on_ready():
    client.loop.create_task(bg())
    #client.loop.create_task(status_task())
    await client.change_presence(game=discord.Game(name='.info | ♥',type=2))
    print('Connected')
    print('Developed by Qwesdy')

# Send Shop Message

#async def status_task():
#    while True:
#        await client.send_message(client.get_channel('495608748488785933'), 'Qwenty je g0d')
#        await asyncio.sleep(1800)
#        await client.send_message(client.get_channel('495608748488785933'), 'Qwenty je g0d')
#        await asyncio.sleep(1800)

# Info Cmd

@client.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(title="Qwenty's Bot Information", description="", colour=ctx.message.author.top_role.colour)
    embed.add_field(name="Commands:", value="** **", inline=False)
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

# Audio

def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))
opts = {
    'default_search': 'auto',
    'quiet': True,
}  # youtube_dl options



load_opus_lib()

servers_songs={}
player_status={}
now_playing={}
song_names={}
paused={}

async def set_player_status():
    for i in client.servers:
        player_status[i.id]=False
        servers_songs[i.id]=None
        paused[i.id]=False
        song_names[i.id]=[]
    print(200)



async def bg():
    client.loop.create_task(set_player_status())

@client.event
async def on_reaction_add(react,user):
    pass


async def check_voice(con):
    pass




async def queue_songs(con,clear):
    if clear == True:
        song_names[con.message.server.id].clear()
        await client.voice_client_in(con.message.server).disconnect()
        player_status[con.message.server.id] = False

    if clear == False:

        if len(song_names[con.message.server.id])==0:
            servers_songs[con.message.server.id]=None

        if len(song_names[con.message.server.id]) !=0:
            song=await client.voice_client_in(con.message.server).create_ytdl_player(song_names[con.message.server.id][0], ytdl_options=opts, after=lambda: client.loop.create_task(after_song(con, False)))
            servers_songs[con.message.server.id]=song
            servers_songs[con.message.server.id].start()
            await client.delete_message(now_playing[con.message.server.id])
            msg=await client.send_message(con.message.channel,"Now playing")
            now_playing[con.message.server.id]=msg

            if len(song_names[con.message.server.id]) >= 1:
                song_names[con.message.server.id].pop(0)


        if len(song_names[con.message.server.id]) ==0 and servers_songs[con.message.server.id] == None:
            player_status[con.message.server.id]=False
        

async def after_song(con,clear):
    client.loop.create_task(queue_songs(con,clear))
    client.loop.create_task(check_voice(con))



@client.command(pass_context=True)
async def play(con,*,url):
    """PLAY THE GIVEN SONG AND QUEUE IT IF THERE IS CURRENTLY SOGN PLAYING"""
    check = str(con.message.channel)
    if check == 'Direct Message with {}'.format(con.message.author.name):
        await client.send_message(con.message.channel, "**You must be in a `server voice channel` to use this command**")

    if check != 'Direct Message with {}'.format(con.message.author.name):
        if client.is_voice_connected(con.message.server) == False:
            await client.join_voice_channel(con.message.author.voice.voice_channel)

        if client.is_voice_connected(con.message.server) == True:
            if player_status[con.message.server.id]==True:
                song_names[con.message.server.id].append(url)
                await client.send_message(con.message.channel, "**Song  Queued**")


                
            if player_status[con.message.server.id]==False:
                player_status[con.message.server.id]=True
                song_names[con.message.server.id].append(url)
                song=await client.voice_client_in(con.message.server).create_ytdl_player(song_names[con.message.server.id][0], ytdl_options=opts, after=lambda: client.loop.create_task(after_song(con,False)))
                servers_songs[con.message.server.id]=song
                servers_songs[con.message.server.id].start()
                msg = await client.send_message(con.message.channel, "Now playing {}".format(servers_songs[con.message.server.id].title))
                now_playing[con.message.server.id]=msg
                song_names[con.message.server.id].pop(0)




@client.command(pass_context=True)
async def skip(con):
    check = str(con.message.channel)
    if check == 'Direct Message with {}'.format(con.message.author.name):#COMMAND IS IN DM
        await client.send_message(con.message.channel, "**You must be in a `server voice channel` to use this command**")

    if check != 'Direct Message with {}'.format(con.message.author.name):#COMMAND NOT IN DM
        if servers_songs[con.message.server.id]== None or len(song_names[con.message.server.id])==0 or player_status[con.message.server.id]==False:
            await client.send_message(con.message.channel,"**No songs in queue to skip**")
        if servers_songs[con.message.server.id] !=None:
            servers_songs[con.message.server.id].pause()
            client.loop.create_task(queue_songs(con,False))



@client.command(pass_context=True)
async def join(con,channel=None):
    """JOIN A VOICE CHANNEL THAT THE USR IS IN OR MOVE TO A VOICE CHANNEL IF THE client IS ALREADY IN A VOICE CHANNEL"""
    check = str(con.message.channel)

    if check == 'Direct Message with {}'.format(con.message.author.name):#COMMAND IS IN DM
        await client.send_message(con.message.channel, "**You must be in a `server voice channel` to use this command**")

    if check != 'Direct Message with {}'.format(con.message.author.name):#COMMAND NOT IN DM
        voice_status = client.is_voice_connected(con.message.server)

        if voice_status == False:#VOICE NOT CONNECTED
            await client.join_voice_channel(con.message.author.voice.voice_channel)

        if voice_status == True:#VOICE ALREADY CONNECTED
            await client.send_message(con.message.channel, "**client is already connected to a voice channel**")



@client.command(pass_context=True)
async def leave(con):
    """LEAVE THE VOICE CHANNEL AND STOP ALL SONGS AND CLEAR QUEUE"""
    check=str(con.message.channel)
    if check == 'Direct Message with {}'.format(con.message.author.name):#COMMAND USED IN DM
        await client.send_message(con.message.channel,"**You must be in a `server voice channel` to use this command**")

    if check != 'Direct Message with {}'.format(con.message.author.name):#COMMAND NOT IN DM
        
        # IF VOICE IS NOT CONNECTED
        if client.is_voice_connected(con.message.server) == False:
            await client.send_message(con.message.channel,"**client is not connected to a voice channel**")

        # VOICE ALREADY CONNECTED
        if client.is_voice_connected(con.message.server) == True:
            client.loop.create_task(queue_songs(con,True))

@client.command(pass_context=True)
async def pause(con):
    check = str(con.message.channel)
    if check == 'Direct Message with {}'.format(con.message.author.name):# COMMAND IS IN DM
        await client.send_message(con.message.channel, "**You must be in a `server voice channel` to use this command**")

    # COMMAND NOT IN DM
    if check != 'Direct Message with {}'.format(con.message.author.name):
        if servers_songs[con.message.server.id]!=None:
            if paused[con.message.server.id] == True:
                await client.send_message(con.message.channel,"**Audio already paused**")
            if paused[con.message.server.id]==False:
                servers_songs[con.message.server.id].pause()
                paused[con.message.server.id]=True

@client.command(pass_context=True)
async def resume(con):
    check = str(con.message.channel)
    # COMMAND IS IN DM
    if check == 'Direct Message with {}'.format(con.message.author.name):
        await client.send_message(con.message.channel, "**You must be in a `server voice channel` to use this command**")

    # COMMAND NOT IN DM
    if check != 'Direct Message with {}'.format(con.message.author.name):
        if servers_songs[con.message.server.id] != None:
            if paused[con.message.server.id] == False:
                await client.send_message(con.message.channel,"**Audio already playing**")
            if paused[con.message.server.id] ==True:
                servers_songs[con.message.server.id].resume()
                paused[con.message.server.id]=False

# Auto role

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member, role)

client.run(TOKEN)
