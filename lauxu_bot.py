import discord
from discord.ext import commands
from config.Settings import Settings

# Import Custom Modules
from modules.e7_tournament import FightClub

client = discord.Client()
fightClub = FightClub()

# Bot Command Prefix
bot = commands.Bot(command_prefix='!')

@bot.command()
async def openTournament(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(Settings.token)
