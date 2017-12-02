import re

from slackbot import bot


@bot.listen_to('show balance[s]?', flags=re.IGNORECASE)
def balances(message):
    # TODO get bank accounts for a single user
    # TODO get balances for all bank accounts for that user
    # TODO format response as attachment in slack
    message.send('Hello Word')
