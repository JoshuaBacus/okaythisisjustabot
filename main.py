import discord
from discord.ext    import commands
from discord.ext.commands   import Bot

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Autoreact ready...')

@bot.event
async def on_message(message):
    if message.channel.id == 715903002090799135: # Hier Server ID einfügen
        await message.add_reaction("👍") # Hier Emoji einsetzen
        await message.add_reaction("👎") # Hier Emoji einsetzen
        await message.add_reaction("💁") # Hier Emoji einsetzen

bot.run("NzE0ODMxMjk3NjAzOTYwODMy.Xtn8wA.TTc6na0MgFAVhNC3DEq_VJFWpH8") # Hier Token einfügen
