# Python 3
# test project for image/link posting bot

import json
import discord
import wikipediaapi

with open('config.json', 'r') as f:
	config = json.load(f)

BOT_TOKEN = config['DISCORD_BOT']['TOKEN']

client = discord.Client()
wiki = wikipediaapi.Wikipedia('en')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$'):
		if message.content.startswith('$s' or '$S' or '$search'):
			print('Message: ', message.content)
			command = message.content.split(' ', 1)
			if len(command) > 1:
				cmd = command[0]
				query = command[1]

				if not query.isspace():
					print('Command: ', cmd)
					print('Query: ', query)
					summ = get_summary(query)

					for seg in summ:
						await message.channel.send(seg)
				else:
					msg = 'You forgot to input a query {0.author.mention}.'.format(message)
					await message.channel.send(message.channel, msg)
			else:
				msg = 'You forgot to input a query {0.author.mention}.'.format(message)
				await message.channel.send(message.channel, msg)
		else:
			msg = 'Not a valid command {0.author.mention}.'.format(message)
			await message.channel.send(msg)
	else:
		return

@client.event
async def on_ready():
	print('Logged in as: ')
	print(client.user.name)
	print(client.user.id)
	print('--------------')
	print()

def get_page(query):
	return wiki.page(query)

def get_summary(query):
	page = get_page(query)
	if page.exists():
		print('Page exists.')
		print('This is the page: ', page)
		return split_summary(page.summary)
	else:
		print('Page does not exist.')
		return ['Not a Wikipedia page.']

def split_summary(summary):
	print(summary)
	sum_len = len(summary)
	if sum_len > 2000:
		return [summary[i:i + 1500] for i in range(0, sum_len, 1500)]
	else:
		return [summary]

client.run(BOT_TOKEN)