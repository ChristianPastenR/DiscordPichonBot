# bot.py
import os
import random
from dotenv import load_dotenv
 
# 1
from discord.ext import commands
 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
 
# 2
bot = commands.Bot(command_prefix='¡')
 
@bot.event
async def on_ready():
    print(f'{bot.user.name} se conecto al servidor!')




#Custom start

@bot.command(name='bot')
async def mensaje(ctx):

 
    response = "que zarpa"
    await ctx.send(response)

#Custom end


















bot.run(TOKEN)