import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

client = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def feidms(ctx):
    await ctx.send('vc')

@bot.command()
async def kirufeio(ctx):
    await ctx.send('concordo')

@bot.command()
async def cat(ctx):
    embed=discord.Embed(
     title="ALEK GAYZAO",
     url="https://www.youtube.com/watch?v=J---aiyznGQ&ab_channel=KeyboardCat2020",
     description="GATO FODA TOCANDO PIANO",
     color=0xFF5733)

    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/en/8/87/Keyboard_cat.jpg')
    embed.add_field(name='Kauantibo', value='viado com certeza', inline=True
    )

    await ctx.send(embed = embed)

bot.run('')