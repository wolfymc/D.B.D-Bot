import discord
from discord.ext import commands

TOKEN = 'NTE5Njc2OTkwMjE1Njg0MTA4.DujFvQ.nTlf-F-DsRkMVZEnufuXEccOmK0'

client = commands.Bot(command_prefix="s!")

extensions = ['cogs.ban', 'cogs.help', 'cogs.joined', 'cogs.kick']
client.remove_command('help') '''removes the default help command, and replaces it with the help command u provided'''

for extension in extensions:
    try:
        client.load_extension(extension)
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def load(ctx, extension):
	try:
		client.load_extension(extension)
		print('Loaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be loaded. [{}]'.format(extension, error))
		
@client.command()
async def unload(ctx, extension):
	try:
		client.unload_extension(extension)
		print('Unloaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be unloaded. [{}]'.format(extension, error))
	
	client.run(TOKEN)
