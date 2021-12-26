import discord
from discord.ext import commands, tasks
import config

TOKEN = ''

@tasks.loop()
async def inform(days=config.DAYS):
    pass
    member: discord.Member = discord.utils.get()
    for role in config.ROLES_TO_LOOK_FOR:
        await member.add_roles(config.ROLES_TO_LOOK_FOR)
