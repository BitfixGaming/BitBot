from discord.ext import commands
import discord
from discord import Game
import traceback
from config import get_section

global bot
bot = commands.Bot(command_prefix=get_section("bot").get("command_prefix", "!"),pm_help=True)

extensions = get_section("bot").get("extensions")

if __name__ == "__main__":

    @bot.event
    async def on_ready():
        print('Connected!')
        print(f'Username: {bot.user.name}')
        print(f'ID: {bot.user.id}')
        await bot.change_presence(activity=Game(name="GGWP"))

    @bot.event
    async def on_raw_reaction_add(payload):
        channel_id = payload.channel_id
        message_id = payload.message_id
        user_id = payload.user_id
        emoji = payload.emoji


        print(emoji)
        print(message_id)

    for extension in extensions:
        try:
            bot.load_extension(extension)
            print(f"Loaded extension {extension}")
        except Exception as e:
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

    print("Connecting to discord")
    bot.run(get_section("bot").get("discord_key"))
