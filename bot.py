# import discord
from discord.ext import commands, tasks
import config

TOKEN = ''
client = commands.Bot(command_prefix="-")

# Convert days to hours cause we can only use hours.
hours = config.DAYS * 24

'''
@tasks.loop(hours=hours)
async def inform(ctx):
    days = config.DAYS
    all_members_in_guild = ctx.guild.members
    for member in all_members_in_guild:
        roles_of_member = member.roles
        for role in roles_of_member:
            await ctx.send("Roles of {}: {}".format(member, role))
'''

@client.command()
async def send(ctx):
    all_members_in_guild = ctx.guild.members
    for member in all_members_in_guild:
        roles_of_member = member.roles
        for role in roles_of_member:
            await ctx.send("Roles of {}: {}".format(member, role))

client.run(TOKEN)
