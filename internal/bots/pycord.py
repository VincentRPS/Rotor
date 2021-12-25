from abc import ABC

from discord.ext.commands import AutoShardedBot


class Interactions(AutoShardedBot, ABC):
    pass
