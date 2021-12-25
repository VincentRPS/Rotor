import discord
from discord.ext import commands
import yaml
from yaml import SafeLoader
from discord.ext.commands import Cog

file = open("internal/config.yml", "r")
raw_data = yaml.load(file, Loader=SafeLoader)
file.close()

class CoreEvents(Cog):
	def __init__(self, interactions):
		self.bot = interactions
	
	@Cog.listener()
	async def on_ready(self):
		guild = await self.bot.fetch_channel(raw_data.get("UPTIME_CHANNEL"))
		await guild.send("Rotor is now spinning again!")
	
	@Cog.listener()
	async def on_command_error(self, error):
		if isinstance(error, commands.CommandNotFound):
			return
		else:
			guild = await self.bot.fetch_channel(raw_data.get("LOGGING_CHANNEL"))
			await guild.send(f"{error}")
			
	@Cog.listener()
	async def on_message(self, message):
		mention = f"<@!{self.client.user.id}>"
		if message.content == mention:
			message.channel.send("Hey! you seemed to of spun my propellers, My current prefix for this server is `%`")
		else:
			guild = await self.bot.fetch_channel(raw_data.get("LOGGING_CHANNEL"))
			await guild.send(f"{message}")


def setup(interactions):
	interactions.add_cog(CoreEvents(interactions))
