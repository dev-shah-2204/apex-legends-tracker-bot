import os
from bot import ApexTracker

cogs = [
    'botstats',
    'developer',
    'apex',
    'help'
]

bot = ApexTracker()
bot.remove_command('help')

for cog in cogs:
    if __name__ == "__main__":
        bot.load_extension(f"cogs.{cog}")
        print(f"{cog}.py loaded")

bot.run("OTMwNDI3MTIwNTg3NTMwMjkw.Yd1tyA.VHV6ECqLBTQWlRhXNaAFVfi0Nd0")
