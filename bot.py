import discord
from discord.ext import commands, tasks
import config
import os
import datetime
import logging
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="-")

# Convert days to hours cause we can only use hours.
hours = int(config.DAYS) * 24

level = logging.INFO
fmt = '[%levelname)s] %(asctime)s - %(message)s'
logging.basicConfig(level=level, format=fmt)


@tasks.loop(minutes=1)
async def inform(ctx):
    all_members_in_guild = ctx.guild.members
    for member in all_members_in_guild:
        roles_of_member = member.roles
        for role in roles_of_member:
            if str(role) in config.ROLES_TO_LOOK_FOR:
                first_time = datetime.datetime.now()
                joined_time = member.joined_at
                diff = first_time - joined_time
                channel: discord.TextChannel = client.get_channel(924811417809481761)
                await channel.send(f"INFO: (Guest) {member.name} has now been on the server for {str(diff.days)} days")
                if str(diff.days) >= str(config.DAYS):
                    await channel.send(f"IMPORTANT: Guest {member.name} has now been on the server for {str(diff.days)} days.")



@client.command()
async def start(ctx):
    ctx.send("Task starting...")
    inform.start(ctx)

@client.event
async def on_ready():
    logging.info("Bot starting...")

client.run(TOKEN)
