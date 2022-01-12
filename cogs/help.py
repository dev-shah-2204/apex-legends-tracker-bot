import discord

from utils import colors
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.command(name='help')
    async def help_command(self, ctx, cmd: str = None):
        if cmd is None:
            em = discord.Embed(
                title="Help is here",
                color=colors.a_red
            )
            em.add_field(
                name="Categories",
                value="Apex\nBot"
            )
            em.set_footer(text="Use 'help <category>' for more info")
            await ctx.reply(embed=em, mention_author=False)

        else:
            aliases = {}
            apex = []
            bot = []


            for command in self.bot.commands:
                aliases[command.name] = []

                if command.cog:
                    if command.cog.qualified_name == 'Apex':
                        apex.append(command.name)
                    elif command.cog.qualified_name == 'BotStats':
                        bot.append(command.name)

                for alias in command.aliases:
                    aliases[command.name].append(alias)

            if cmd.lower() == 'apex':
                desc = ""
                for com in apex:
                    desc += f"`{com}`\n"

                em = discord.Embed(
                    title="Apex commands:",
                    description=desc,
                    color=colors.a_red
                )
                await ctx.reply(embed=em, mention_author=False)

            elif cmd.lower() == 'bot':
                desc = ""
                for com in bot:
                    desc += f"`{com}`\n"

                em = discord.Embed(
                    title="Bot Stats commands:",
                    description=desc,
                    color=colors.a_red
                )
                await ctx.reply(embed=em, mention_author=False)

            else:
                command = discord.utils.get(self.bot.commands, name=cmd.lower())

                if command is None:  # Gotta check if they entered an alias that they're familiar with
                    for com in aliases:
                        for als in aliases[com]:
                            if als == cmd.lower():
                                command = discord.utils.get(self.bot.commands, name=com)
                                break

                    if command is None:  # If still none after checking for aliases
                        await ctx.reply("That command does not exist", mention_author=False)
                        return

                _aliases = ", ".join([*command.aliases])
                if _aliases == '':
                    _aliases = "This command has no aliases"

                _help = command.help
                if _help is None:
                    _help = "No information"

                args = []
                for key, value in command.params.items():
                    if key not in ("self", "ctx"):
                        if "None" in str(value) or "No reason provided" in str(value):  # If that param is optional
                            args.append(f"[{key}]")
                        else:
                            args.append(f"<{key}>")

                args = " ".join(args)

                em = discord.Embed(
                    title=command.name.capitalize(),
                    description=_help,
                    color=colors.a_red
                )
                em.add_field(
                    name="Usage:",
                    value=f"```{command.name} {args}```",
                    inline=False
                )
                em.add_field(
                    name="Aliases",
                    value=_aliases
                )
                await ctx.reply(embed=em, mention_author=False)


def setup(bot):
    bot.add_cog(Help(bot))
