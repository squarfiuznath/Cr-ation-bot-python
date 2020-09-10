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

#lancer le Bot
bot.run("Token")