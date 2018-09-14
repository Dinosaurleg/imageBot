# Python 3
# test project for image/link posting bot

import discord
import json

with open('config.json', 'r') as f:
	config = json.load(f)

BOT_TOKEN = config['DISCORD_BOT']['TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!hello'):
		msg = 'Hello {0.author.mention'.format(message)
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as: ')
	print(client.user.name)
	print(client.user.id)
	print('--------------')

client.run(BOT_TOKEN)