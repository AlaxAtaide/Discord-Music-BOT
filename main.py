import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def feidms(ctx):
    await ctx.send('é o kiru')
    
bot.run('MTAyOTgxOTc0NjkxODYwMDc4NA.GKl2JY.NVf1L7zob9dNBk7nRy7NpodEx4mUTPyfZdzj88')