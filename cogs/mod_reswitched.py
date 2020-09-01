import config
from discord.ext import commands
from discord.ext.commands import Cog
from helpers.checks import check_if_staff


class ModReswitched(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(aliases=["pingmods", "summonmods"])
    async def pingmod(self, ctx):
        """Pings mods, only use when there's an emergency and such."""
        can_ping = any(r.id in config.pingmods_allow for r in ctx.author.roles)
        if can_ping:
            await ctx.send(
                f"<@&{config.pingmods_role}>: {ctx.author.mention} needs assistance."
            )
        else:
            await ctx.send(
                f"{ctx.author.mention}: You need community to be able to ping the entire staff team, please pick an online staff member, check if they have the mod role, and ping them instead."
            )

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command()
    async def modtoggle(self, ctx):
        """Toggles your mod role, staff only."""
        target_role = ctx.guild.get_role(config.modtoggle_role)

        if target_role in ctx.author.roles:
            await ctx.author.remove_roles(
                target_role, reason="Staff self-unassigned mod role"
            )
            await ctx.send(f"{ctx.author.mention}: Removed your mod role.")
        else:
            await ctx.author.add_roles(
                target_role, reason="Staff self-assigned mod role"
            )
            await ctx.send(f"{ctx.author.mention}: Gave you mod role.")


def setup(bot):
    bot.add_cog(ModReswitched(bot))