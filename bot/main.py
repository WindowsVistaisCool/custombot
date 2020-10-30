import discord
import json
from discord.ext import commands

def store(file, key, val=None, read=False):
	with open(file, 'r') as v:
		x = json.load(v)
	if read is not False:
		return x[key]
	else:
		x[key] = val
		with open(file, 'w') as v:
			json.dump(x, v, indent=4)

prefix = store('.config.json', 'prefix', read=True)
token = store('.config.json', 'token', read=True)
client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
	print(f"Ready\n({client.user}, {client.user.id})")
	acttype = store('.config.json', 'acttype', read=True)
	act = store('.config.json', 'act', read=True)
	if acttype == "game":
		await client.change_presence(activity=discord.Game(name=act))
	elif acttype == "watch":
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching(), name=act))
	elif acttype == "listen":
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening(), name=act))

client.run(token)
