from discord.ext import commands
from config import get_section
from discord import *


class reactionranker(commands.Cog):

    least_role_needed = get_section("bot").get("admin_minimum_role")

    def __init__(self, bot):
        self.bot = bot

    def has_at_least_role(name):
        def predicate(ctx):
            msg = ctx.message
            ch = msg.channel
            if type(ch) == DMChannel:
                return False

            role = utils.get(ctx.guild.roles, name=name)

            return any([x >= role for x in msg.author.roles])

        return commands.check(predicate)

    @commands.command(aliases=["addreactions"])
    @has_at_least_role(least_role_needed)
    async def addreact(self, ctx, messageid: int):
        """Adds base reactions to specified message (Admin only)"""

        if messageid is not None:
            msg = await ctx.fetch_message(id=messageid)
            for emojiId in get_section("bot").get("ranks"):
                await msg.add_reaction(emoji=str(emojiId))

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == int(get_section("bot").get("rank_channel_id")):
            discorduser = utils.get(Client.get_all_members(self.bot), id=payload.user_id)
            if utils.get(discorduser.guild.roles, id=int(get_section("bot").get("ranks").get(payload.emoji.name))) in discorduser.roles:
                await discorduser.remove_roles(utils.get(discorduser.guild.roles, id=int(get_section("bot").get("ranks").get(payload.emoji.name))))

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.channel_id == int(get_section("bot").get("rank_channel_id")):
            discorduser = utils.get(Client.get_all_members(self.bot), id=payload.user_id)
            await discorduser.add_roles(utils.get(discorduser.guild.roles, id=int(get_section("bot").get("ranks").get(payload.emoji.name))))


def setup(bot):
    bot.add_cog(reactionranker(bot))
