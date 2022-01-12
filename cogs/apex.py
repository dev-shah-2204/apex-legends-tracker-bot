import requests
import os
import discord

from discord.ext import commands
from discord.ext.commands import command, cooldown, BucketType

from utils import colors


class Apex(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = os.getenv('APEX_LEGENDS_API_KEY')


    @command(name="profile")
    async def get_player(self, ctx, origin_name):
        response = requests.get(url=f"https://api.mozambiquehe.re/bridge?version=5&player={origin_name}&platform=PC&auth={self.api_key}")
        result = response.json()

        if 'Error' in result:
            print(result)
            await ctx.reply(f"Player with name `{origin_name}` was not found", mention_author=False)
            return

        r = result['global']
        print(r)
        em = discord.Embed(
            title=f"Stats for {r['name']}",
            color=colors.a_red
        )
        em.add_field(
            name="Level:",
            value=f"{r['level']} ({100 - r['toNextLevelPercent']}% progress left for level {r['level'] + 1})",
            inline=False
        )
        em.add_field(
            name="Battle Royale Rank",
            value=f"{r['rank']['rankName']} {r['rank']['rankDiv']} (RP: {r['rank']['rankScore']})",
            inline=False
        )
        em.set_thumbnail(url=r['rank']['rankImg'])

        if r['arena']['rankName'] == 'Unranked':
            pos = ""
        else:
            pos = r['arena']['rankDiv']

        em.add_field(
            name="Arenas Rank",
            value = f"{r['arena']['rankName']} {pos} (AP: {r['arena']['rankScore']})"
        )
        em.add_field(
            name="Current Legend:",
            value=result['legends']['selected']['LegendName'],
            inline=False
        )
        em.set_footer(text=f"Player UID: {r['uid']}")

        await ctx.reply(embed=em, mention_author=False)


    @command(name="crafting")
    async def get_crafting_rotations(self, ctx):
        response = requests.get(f"https://api.mozambiquehe.re/crafting?&auth={self.api_key}")
        result = response.json()

        item_list = []

        for dct in result:
            if not dct['bundleType'] == "permanent":
                for items in dct['bundleContent']:
                    item_list.append(f"{items['itemType']['name']} ({items['itemType']['rarity']})")

        desc = ""
        for item in item_list:
            desc += f"{item.replace('_', ' ').title()}\n"

        em = discord.Embed(
            title="Current Crafting Rotation",
            description=desc,
            color=colors.a_red
        )
        await ctx.reply(embed=em, mention_author=False)



def setup(bot):
    bot.add_cog(Apex(bot))

if __name__ == "__main__":
    raise RuntimeError("Make sure you're running the main.py file, not the bot.py file")
