# Collecting usernames with a telegram Bot
This is a simple Telegram bot built using `python-telegram-bot` library that listens to users, replies to basic messages, and collects their usernames for future reference.
The bot saves unique usernames to a local JSON file (`usernames.json`) when users send commands or text messages.
## Requirements
- Python 3.8+
- python-telegram-bot library
- requests library
## Installation
- create an empty folder in VSCode
- open terminal
- enter cmd
- create virtual venv use python `-m venv .venv`
- activate venv by `.venv\srcrippts\activate`
- install requests `pip install requests`
- install telegram library `pip install python-telegram-bot`
## How It Works
This bot is designed to collect and store unique Telegram usernames of users who interact with it. Here's a breakdown of how the bot works:

1. User Interaction

   The bot listens for messages and commands. Upon receiving any interaction, it checks if the user has a valid username to save.
2. Username Extraction

   The bot checks if the user has a valid and publicly available username in their Telegram profile. If a username exists, it will be processed for storage.
3. Avoiding Duplicates

   It ensures that each username is only saved once. If a username is already in the list of saved usernames (`usernames.json`), it will not be added again.
4. Saving Usernames to File

   Once a new username is detected, it is added to an internal list and then written to a local JSON file (`usernames.json`)
5. File Structure

   The `usernames.json` file holds the usernames in a simple array format.
   This file is updated dynamically each time a new user interacts with the bot for the first time.