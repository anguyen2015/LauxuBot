from discord.ext import commands
from config.Settings import Settings

# Import Custom Modules
from modules.e7_tournament import FightClub

fightClub = FightClub()

# Bot Command Prefix
bot = commands.Bot(command_prefix='!')

@bot.command()
async def user_is_me(ctx):
    await ctx.send(ctx.message.author.id)

@bot.command()
async def openTournament(ctx, arg):
    success = fightClub.handleCreateTournament(arg)
    if success:
        await ctx.send("{0} has started.".format(arg))
    else:
        await ctx.send("Failed to start a new Tournament, one is currently open.")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(Settings.token)
