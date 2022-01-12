import discord
import os

from discord.ext import commands


class ApexTracker(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=">>",
            intents=discord.Intents.all(),
            case_insensitive=True,
            allowed_mentions=discord.AllowedMentions(everyone=False), # (everyone:bool, users:bool, roles:bool, replied_user:bool)
            owner_id=416979084099321866  # Your ID here
        )

    async def on_ready(self):
        print("^_^")
        print(f"Logged in as {self.user}")
        print(f"ID: {self.user.id}")


if __name__ == "__main__":
    raise RuntimeError("Make sure you're running the main.py file, not the bot.py file")
