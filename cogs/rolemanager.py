from discord.ext import commands
from discord.utils import get, find
from config import get_section
import discord


class Rolemanager(commands.Cog):
    """Allows you to throw some dice using standard dice notation."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addrole(self, ctx, member: discord.Member, *, rolename: discord.Role):
        await ctx.channel.trigger_typing()
        for x in get_section("managedroles"):
            sectionRole = find(lambda r: r.id == x, ctx.message.author.roles)
            if sectionRole in ctx.message.author.roles:
                if str(rolename.id) in get_section("managedroles").get(sectionRole.id):
                    if rolename in member.roles:
                        await ctx.send("⚠ " + member.display_name + " already has " + rolename.name)
                        break
                    else:
                        await ctx.send("Added " + rolename.name + " to " + member.display_name)
                        await member.add_roles(rolename)
                        break
            else:
                await ctx.send("⚠ You're not allowed to give other users " + rolename.name)
                break

    @addrole.error
    async def addrole_error(self, ctx, error):
        await ctx.send(str(error))

    @commands.command()
    async def removerole(self, ctx, member: discord.Member, *, rolename: discord.Role):
        await ctx.channel.trigger_typing()
        for x in get_section("managedroles"):
            sectionRole = find(lambda r: r.id == x, ctx.message.author.roles)
            if sectionRole in ctx.message.author.roles:
                if str(rolename.id) in get_section("managedroles").get(sectionRole.id):
                    if rolename in member.roles:
                        await member.remove_roles(rolename)
                        await ctx.send("Removed " + rolename.name + " from " + member.display_name)
                        break
                    else:
                        await ctx.send("⚠ " + member.display_name + " does not have " + rolename.name)
                        break
            else:
                await ctx.send("⚠ You're not allowed to remove " + rolename.name + " from other users")
                break

    @removerole.error
    async def removerole_error(self, ctx, error):
        await ctx.send(str(error))

def setup(bot):
    bot.add_cog(Rolemanager(bot))
