import datetime
import discord
import os
import random
import re
import string
from discord.ext import commands
from sys import argv

class Extras:
    """
    Extra things.
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    prune_key = "nokey"

    @commands.command()
    async def membercount(self):
        """Prints the member count of the server."""
        await self.bot.say("{} has {:,} members!".format(self.bot.server.name, self.bot.server.member_count))

    @commands.has_permissions(ban_members=True)
    @commands.command(hidden=True)
    async def embedtext(self, *, text):
        """Embed content."""
        await self.bot.say(embed=discord.Embed(description=text))


    @commands.has_permissions(manage_nicknames=True)
    @commands.command()
    async def estprune(self, days=30):
        """Estimate count of members that would be pruned based on the amount of days. Staff only."""
        if days > 30:
            await self.bot.say("Maximum 30 days")
            return
        if days < 1:
            await self.bot.say("Minimum 1 day")
            return
        msg = await self.bot.say("I'm figuring this out!".format(self.bot.server.name))
        count = await self.bot.estimate_pruned_members(server=self.bot.server, days=days)
        await self.bot.edit_message(msg, "{:,} members inactive for {} day(s) would be kicked from {}!".format(count, days, self.bot.server.name))

    @commands.has_permissions(manage_nicknames=True)
    @commands.command(pass_context=True)
    async def prune30(self, ctx, key=""):
        """Prune members that are inactive for 30 days. Staff only."""
        if self.bot.pruning > 0:
            await self.bot.say("Pruning is already in progress.")
            return
        if key != self.prune_key:
            if key != "":
                await self.bot.say("That's not the correct key.")
            self.prune_key = ''.join(random.sample(string.ascii_letters, 8))
            await self.bot.say("Are you sure you want to prune members inactive for 30 days?\nTo see how many members get kicked, use `.estprune`.\nTo confirm the prune, use the command `.prune30 {}`.".format(self.prune_key))
            return
        self.prune_key = ''.join(random.sample(string.ascii_letters, 8))
        await self.bot.say("Starting pruning!")
        count = await self.bot.prune_members(self.bot.server, days=30)
        self.bot.pruning = count
        await self.bot.send_message(self.bot.mods_channel, "{:,} are currently being kicked from {}!".format(count, self.bot.server.name))
        msg = "👢 **Prune**: {} pruned {:,} members".format(ctx.message.author.mention, count)
        await self.bot.send_message(self.bot.modlogs_channel, msg)

    @commands.has_permissions(manage_nicknames=True)
    @commands.command()
    async def disableleavelogs(self):
        """DEBUG COMMAND"""
        self.bot.pruning = True
        await self.bot.say("disable")

    @commands.has_permissions(manage_nicknames=True)
    @commands.command()
    async def enableleavelogs(self):
        """DEBUG COMMAND"""
        self.bot.pruning = False
        await self.bot.say("enable")
		
def setup(bot):
    bot.add_cog(Extras(bot))
