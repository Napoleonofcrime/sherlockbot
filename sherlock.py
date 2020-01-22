import discord
from discord.ext import commands

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
 print('bot is ready')
 client.run('NjUzODQwMjIxMDA3MjQ5NDE4.Xib4CQ.eHfq8xKekFH2iMMnh7XuMxjOzxs')