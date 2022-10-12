import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def feidms(ctx):
    await ctx.send('vc')

@bot.command()
async def kirufeio(ctx):
    await ctx.send('concordo')

@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="ALEK GAYZAO", url="https://upload.wikimedia.org/wikipedia/en/8/87/Keyboard_cat.jpg", description="GATO FODA TOCANDO PIANO", color=0xFF5733)
    await ctx.send(embed=embed)

bot.run('MTAyOTgxOTc0NjkxODYwMDc4NA.Gj90FW.-PGGJ-WiOIKMLyBkwSOAIaFkuBVTb1BPFAdVHA')