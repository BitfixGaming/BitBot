from discord.ext import commands
from config import get_section
from discord import *


class reactionranker(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == int(get_section("bot").get("rank_channel_id")) and str(payload.emoji) == "👍":
            member = utils.get(Client.get_all_members(self.bot), id=payload.user_id)
            await member.add_roles(utils.get(member.guild.roles, id=609083237708333156))

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.channel_id == int(get_section("bot").get("rank_channel_id")) and (str(payload.emoji) == "👍"):
            member = utils.get(Client.get_all_members(self.bot), id=payload.user_id)
            if utils.get(member.guild.roles, id=609083237708333156) in member.roles:
                await member.remove_roles(utils.get(member.guild.roles, id=609083237708333156))


def setup(bot):
    bot.add_cog(reactionranker(bot))
