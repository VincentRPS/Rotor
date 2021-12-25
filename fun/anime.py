import discord
from discord.commands.commands import Option, slash_command
from discord.ext.commands import Cog


class Anime(Cog):
	def __init__(self, interactions):
		self.bot = interactions
	pass


def setup(interactions):
	interactions.add_cog(Anime(interactions))
