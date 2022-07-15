import os
import discord

# --- Change the configuration for run. ---

# 1- bot token (change it, keep it secret)
TOKEN = os.environ.get('DS_TOKEN_BOT_1')

# 2- local path to play music
LOCAL_PATH =  os.environ.get("MUSIC_PLAY_PATH")

# 3- channel id for welcome message
WELCOME_CHANNEL_ID =  os.environ.get("DS_ID")

# 4- coin market cap api key for cryptocurrency commands
COINMARKETCAP_API_KEY = os.environ.get("COINMARKETCAP_API_KEY")

# command prefix
COMMAND_PREFIX = '='

# description
DESCRIPTION = 'A bot for the discord server'

# intents
INTENTS = discord.Intents.all()
INTENTS.members = True

#  your id for leave message
AUTHOR_ID =  os.environ.get("AUTHOR_ID") #DELETE THIS LINE

