import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
 
bot = commands.Bot(command_prefix='whatever_prefix_u_want_here')
 
@bot.event
async def on_ready():
    print ("whatever_text_u_want_here")
 
 
@bot.event
async def on_message(message):
    if(message.channel.id == "714830123190452344"):
        await bot.add_reaction(message, "<:letterTealW:560705837413171211>")
 
 
bot.run("NzE1Nzk3NDkzNDc2MjI5MTgw.XtCmMA.GiHZSL3lSvuIprn0S2FDHZqYn7E")