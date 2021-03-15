import googletrans
import discord
import re

# Globals
LOGGING = False				# Set to true if you want the bot to log to the console
DEFAULT_LANGUAGE = "en"		# Change to edit your default language

# Loads token from token.txt
f = open("token.txt", "r")
bot_token = f.read()

# Initialization
client = discord.Client()
tr = googletrans.Translator()

# Connected Message
@client.event
async def on_ready():
	if LOGGING:
		print("Connected")

@client.event
async def on_message(message):
	if message.author == client.user:
		# Dont respond to own messages
		return

	elif message.content == "[tr help]":
		# Help message
		HELP_MESSAGE =  "Syntax: [tr]\n"
		HELP_MESSAGE += "Arguments (optional): s (source language), d (destination language)\n\n"
		HELP_MESSAGE += "Example: [tr s=en d=fr] I am hungry.\n"
		HELP_MESSAGE += "Another Example: [tr] Tu es mon ami.\n\n"
		HELP_MESSAGE += "[tr languages] for a list of languages and codes"
		await message.reply(HELP_MESSAGE, mention_author=True)

	elif message.content == "[tr languages]":
		# List of languages
		output = "code: language\n\n"
		for key in googletrans.LANGUAGES:
			output += key
			output += ": "
			output += googletrans.LANGUAGES.get(key).capitalize()
			output += "\n"
		await message.reply(output, mention_author=False)

	elif (message.content.startswith('[tr ') and ']' in message.content) or message.content.startswith('[tr]'):
		# Split message into command and text
		end = message.content.index(']')
		args = message.content[1: end]
		text = message.content[end + 2:]

		# Check if text is valid (non empty)
		if text == None or text.isspace() or text == "":
			emb = discord.Embed(title="Error", description='Please include a message to translate. Use [tr help] for help.', color=0x00ff00)
			await message.reply(embed=emb, mention_author=False)
			return

		# Split command into arguments
		args = re.split(" |=", args)
		while "" in args: args.remove("")

		srcArg = False			# True if source language was provided

		# Check if source langauge given as argument, if not try to detect
		try:
			srcind = args.index("s")
			src = args[srcind + 1]
			srcArg = True
		except ValueError:
			src = tr.detect(text)
			src = src.lang

		# Check if destination language given as argument, if not set to DEFAULT_LANGUAGE
		try:
			dstind = args.index("d")
			dst = args[dstind + 1]
			dstArg = True
		except ValueError:
			dst = DEFAULT_LANGUAGE

		# Check if source language is valid, if not send error
		if src in googletrans.LANGUAGES:
			srcLang = googletrans.LANGUAGES.get(src).capitalize()
		else:
			emb = discord.Embed(title="Error", description='Invalid Source Language.', color=0x00ff00)
			await message.reply(embed=emb, mention_author=False)

		# Check if destination language is invalid, if yes send error
		if not dst in googletrans.LANGUAGES:
			emb = discord.Embed(title="Error", description='Invalid Destination Language.', color=0x00ff00)
			await message.reply(embed=emb, mention_author=False)

		# Generate translation, log message details, then send message
		output = tr.translate(text, src=src, dest=dst)
		if LOGGING:
			print(src, "|", dst, "|", text, "|", output.text)

		emb = discord.Embed(title="Translated Text", description=output.text, color=0x00ff00)
		if not srcArg: emb.add_field(name="Source Language", value=srcLang, inline=False)
		await message.reply(embed=emb, mention_author=False)

# Runs the bot
client.run(bot_token)
