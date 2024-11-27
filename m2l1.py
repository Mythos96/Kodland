import os
import discord
from bilgi import *
from ayarlar import *
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

    activity = discord.Game("!help")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command()
async def merhaba(ctx):
    await ctx.send('Selam')

@bot.command()
async def bye(ctx):
    await ctx.send('\U0001f642')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(f"{left} + {right} = {left + right}")

@bot.command()
async def şifre(ctx):   
    user = ctx.author
    await user.send(f"Şifreniz: {sifre_olusturucu()}")
    await ctx.send(f"{user.mention} Şifreniz DM ile göderildi!")

@bot.command()
async def coin(ctx):
    await ctx.send(yazi_tura())

@bot.command()
async def ranmoji(ctx):
    await ctx.send(emoji_olusturucu())

@bot.command()
async def shutdown(ctx):
    if ctx.author.id == owner:
        await ctx.send("{Logging off}")
        await bot.close
    else:
        await ctx.send("Bu komutu kullanmak için yetkiniz yok!")

@bot.command()
async def ping(ctx):
    if ctx.author.id == owner:
        latency = round(bot.latency * 1000)
        await ctx.send(f"pong! {latency}ms")
    else:
        await ctx.send("Bu komutu kullanmak için yetkiniz yok!")

@bot.command()
async def help(ctx):
    await ctx.send("Myth Bot Komutları:\n- !merhaba\n- !bye\n- !şifre\n- !coin\n- !ranmoji \n- !add\n\nYetkili komutları:\n- !shutdown\n- !ping")

@bot.command
async def meem(ctx):
    memler_folder = 'memler'
    random_file = random.choice(os.listdir(memler_folder))
    with open(f'{memler_folder}/{random_file}', 'rb') as file:
        picture = discord.File(file)
        await ctx.send(file=picture)

bot.run(token)
