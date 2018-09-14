# Python 3
# test project for image/link posting bot

import discord
import json

with open('config.json', 'r') as f:
	config = json.load(f)

BOT_TOKEN = config['DISCORD_BOT']['TOKEN']