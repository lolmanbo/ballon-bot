#Ballon bot by Jesssestaff#0010

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print ("im ready bro")

@bot.command(pass_context=True)
async def ping(ctx):
        await bot.say("shut up faggot")
        print ("user has been told to shut the hell up")
    
    
bot.run("put id here")
