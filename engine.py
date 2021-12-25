import logging
import os

import discord
import yaml

from internal.bots import pycord

logging.basicConfig(level=logging.INFO)
_log = logging.getLogger(__name__)

try:
    from yaml import CSafeLoader as SafeLoader
except ImportError:
    from yaml import SafeLoader

interactions = pycord.Interactions(commands_prefix="%", intents=discord.Intents.all())

file = open("internal/config.yml", "r")
raw_data = yaml.load(file, Loader=SafeLoader)
file.close()

for module in os.listdir("./fun"):
    if module.endswith(".py"):
        interactions.load_extension(f"fun.{module[:-3]}")
        _log.info(f"{module} has just loaded!")

for module in os.listdir("./events"):
    if module.endswith(".py"):
        interactions.load_extension(f"events.{module[:-3]}")
        _log.info(f"{module} has just loaded!")

interactions.run(raw_data.get("TOKEN"))
