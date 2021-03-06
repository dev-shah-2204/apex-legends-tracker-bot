import os
from bot import ApexTracker

cogs = [
    'botstats',
    'developer',
    'apex',
    'help',
    'error_handler'
]

bot = ApexTracker()
bot.remove_command('help')

for cog in cogs:
    if __name__ == "__main__":
        bot.load_extension(f"cogs.{cog}")
        print(f"{cog}.py loaded")

bot.load_extension("jishaku")

bot.run(os.getenv('APEX_LEGENDS_BOT_TOKEN'))
