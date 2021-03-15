# GoogleTranslateBot

Discord Bot that can translate messages.

# Commands
Format: `[tr s=<source_langague> d=<destination_langauge>]` <text>

Arguments for both source and destination languages are optional. If the source language is not provided, the bot will attempt to detect the language. If the destination langauge is not provide, the bot will default to `DEFAULT_LANGUAGE` (which is set to en, for English).

Special Commands:

`[tr help]`: Displays a help message

`[tr langauges]`: Lists the various languages with their codes

# Installation
### Dependencies
The bot requires discord.py

`pip install discord.py`

It also requires googletrans, of version 3.1.0a0 or above

`pip install -Iv googletrans==3.1.0a0`

### Setup
The only setup that needs to be done is creating a text file, bot.txt. The contents of this file should be your bot token. No such file is provided, due to the sensitive nature of the token.

### Running the bot
You can run the bot with `python bot.py`

### Settings
You can easily change the default language from `en` to any other code of your choice, by the `DEFAULT_LANGUAGE` variable. You can also enable or disable logging with the `LOGGING` variable, which is set to false by default.
