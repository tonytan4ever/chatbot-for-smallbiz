import datetime
import re

from slackbot import bot

from . import utils


@bot.listen_to('Good morning chatbot|GM chatbot', flags=re.IGNORECASE)
def morning_call(message):
    message.send('Good morning from chatbot @ {now}'.format(
      now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )


@bot.listen_to('hello chatbot', flags=re.IGNORECASE)
def greeting_user(message):
    user_name_from_message = utils.get_user_name_from_message(message)
    message.send('Hello %s' % user_name_from_message)


@bot.listen_to('chatbot DM me please', flags=re.IGNORECASE)
def greeting_DM_to_user(message):
    user_name_from_message = utils.get_user_name_from_message(message)
    utils.direct_reply_to_message(
        message,
        'Hello %s, you asked me to DM you' % user_name_from_message)
