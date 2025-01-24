import discord
from discord.ext import commands
from botlogic import generador
from botlogic import gira_una_moneda
from botlogic import gen_emoji
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def gen(ctx):
    await ctx.send(f"Tu contraseña generada es: {generador(10)}")

@bot.command()
async def moneda(ctx):
    await ctx.send(f"La moneda callo y dio: {gira_una_moneda()}")

@bot.command()
async def emogi(ctx):
    await ctx.send(f" {gen_emoji()}")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

bot.run("PON TU TOKEN SECRETO")
