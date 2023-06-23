import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command()
async def greet(ctx, *, name):
    await ctx.send(f'Greetings, {name}!')

bot.run('your_token_here')
