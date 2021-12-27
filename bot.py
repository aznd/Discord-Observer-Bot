import discord
from discord.ext import commands, tasks
import config
import os
import datetime
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="-")

# Convert days to hours cause we can only use hours.
hours = config.DAYS * 24


@tasks.loop(hours=hours)
async def inform(ctx):
    all_members_in_guild = ctx.guild.members
    for member in all_members_in_guild:
        roles_of_member = member.roles
        for role in roles_of_member:
            if role in config.ROLES_TO_LOOK_FOR:
                now_time = datetime.datetime.now()
                joined_time = member.joined_at
                diff = now_time - joined_time
                channel: discord.TextChannel = client.get_channel(924811417809481761)
                await channel.send(f"INFO: (Guest) {member.name} has now been on the server for {str(diff.days)}")
                if str(diff.days) == str(config.DAYS):
                    await channel.send(f"IMPORTANT: Guest {member.name} has now been {str(diff.days)} on the server.")



@client.command()
async def send(ctx):
    all_members_in_guild = ctx.guild.members
    for member in all_members_in_guild:
        roles_of_member = member.roles
        for role in roles_of_member:
            if str(role) in config.ROLES_TO_LOOK_FOR:
                first_time = datetime.datetime.now()
                joined_time = member.joined_at
                diff = first_time - joined_time
                channel: discord.TextChannel = client.get_channel(924811417809481761)
                await channel.send(f"INFO: (Guest) {member.name} has now been on the server for {str(diff.days)}")
                if str(diff.days) == str(config.DAYS):
                    await channel.send(f"IMPORTANT: Guest {member.name} has now been {str(diff.days)} on the server.")


client.run(TOKEN)
