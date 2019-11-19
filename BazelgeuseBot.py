import discord
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import CommandNotFound
import time
import asyncio
import os

bot = commands.Bot(command_prefix = "bazelgeuse ")

@bot.event
async def on_ready():
    print("Bazelgeuse is ready!")

@bot.event
async def on_command_error(context, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

# The following function has Bazelgeuse scream on command
@bot.command()
async def scream(context):
    channel = context.message.author.voice.channel
    if not channel:
        await context.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=context.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    # get path to audio file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    audio = os.path.join(dir_path, "bazelgeuse_scream.mp4.mp4")
    voice.play(discord.FFmpegPCMAudio(audio), after=lambda e: print('done screaming', e))

# The following function tries to make Bazelgeuse leave the channel
# on command !leave, but Bazelgeuse doesn't actually leave the channel
# on command because of the on_voice_state_update function
# and Bazelgeuse does what it wants
@bot.command(pass_context=True)
async def leave(context):
    response = "no  😈"
    await context.message.channel.send(response)
    voice = get(bot.voice_clients, guild=context.guild)
    if voice and voice.is_connected():
        await voice.disconnect()

# The following function has Bazelgeuse scream at anyone
# that joins a voice channel
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel:
        channel = before.channel
    elif after.channel:
        channel = after.channel
    else:
        return
    try:
        voice = await channel.connect()
        if voice and voice.is_connected():
            await voice.move_to(channel)
        # get path to audio file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        audio = os.path.join(dir_path, "bazelgeuse_scream.mp4.mp4")
        voice.play(discord.FFmpegPCMAudio(audio), after=lambda e: print('done screaming', e))
    except discord.ClientException:
        print('Already logged in, but don\'t care')

# The following function has Bazelgeuse react
# to its name being mentioned
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "bazelgeuse no":
        response = "bazelgeuse yes  😈"
        await message.channel.send(response)
    elif message.content == "bazelgeuse leave":
        # do nothing, this is already a command to
        # the leave function, and we don't want
        # bazelgeuse to react twice
        print('')
    else:
        # responds to its name being used in any text channel
        if 'bazelgeuse' in message.content:
            # sends a picture of itself if someone requests nudes
            if 'nudes' in message.content:
                dir_path = os.path.dirname(os.path.realpath(__file__))
                pic = os.path.join(dir_path, "bazelgeuse_pic.png")
                await message.channel.send(file=discord.File(pic))
            elif 'gtfo' in message.content:
                response = "no  😈"
                await message.channel.send(response)
            else:
                response = "roar  😈"
                await message.channel.send(response)
    # need the following line for other commands to work
    await bot.process_commands(message)

bot.run("NjQ0ODI3MTkxMzU5NTY5OTMw.Xc5tqQ.Xo19Sqtr65Y34GS_Tp2BPZ9tpUM")
