#installer les modules
import discord
from discord.ext import commands

#creer le prefix du Bot
bot = commands.Bot(command_prefix = "!", description = "Bot de squarfiuz07 et de nath")

#changer l'activité du Bot
@bot.event
async def on_ready():
  activity = discord.Game(name = "!help", type = 3)
  await bot.change_presence(status = discord.Status.online, activity=activity)
  print("Bot prêt")

#premiere commande
@bot.command()
async def message(ctx):
  await ctx.send("Ceci est un message test.")

#description du serveur
@bot.command()
async def info(ctx):
  server = ctx.guild
  numberOfTextChannels = len(server.text_channels)
  numberOfVoiceChannels = len(server.text_channels)
  numberOfPerson = server.member_count
  serverName = server.name
  message = f"Dans le serveur {serverName} il y a {numberOfPerson} personnes. Le serveur est composé de {numberOfTextChannels} salons écrits et de {numberOfVoiceChannels} salons vocaux"
  await ctx.send(message)

#lancer le Bot
bot.run("Token")
