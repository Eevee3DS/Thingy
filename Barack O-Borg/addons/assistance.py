import discord
from discord.ext import commands
from sys import argv

class Assistance:

    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    async def simple_embed(self, text, title="", color=discord.Color.default()):
        embed = discord.Embed(title=title, color=color)
        embed.description = text
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def stream(self, ctx, *, console="auto"):
        """Links To My Stream"""
        embed = discord.Embed(title="Steven's Stream", color=discord.Color(0x009AC7))
        embed.set_author(name="Stevenwoahh", url="https://www.twitch.tv/stevenwoahh")
        embed.set_thumbnail(url="http://static-cdn.jtvnw.net/jtv_user_pictures/stevenwoahh-profile_image-c9b9237c5b393ff1-300x300.png")
        embed.url = "https://www.twitch.tv/stevenwoahh"
        embed.description = "Come Join Me Streaming"
        await self.bot.say("", embed=embed)

    @commands.command(pass_context=True)
    async def cmds(self):
        """List Cmds"""
        embed = discord.Embed(title="Commands", color=discord.Color(0x0000ff))
        embed.set_thumbnail(url="https://www.twitch.tv/stevenwoahh")
        embed.url = "https://www.twitch.tv/stevenwoahh"
        embed.description = "!battletag\n!discord\n!donate\n!instagram\n!snapchat\n!twitter"
        await self.bot.say("", embed=embed)        

def setup(bot):
    bot.add_cog(Assistance(bot))
