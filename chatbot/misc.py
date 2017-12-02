import datetime
import json
import re

import requests
from slackbot import bot, settings

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


@bot.listen_to('render this', flags=re.IGNORECASE)
def render_this(message):
    json_block = requests.get(message.body['file']['url_private_download'],
                              headers=dict(Authorization="Bearer %s" % settings.API_TOKEN)).text
    try:
        json.loads(json_block)
    except Exception:
        message.reply("This is not a valid json block/No json uploaded")
    else:
        message.send_webapi("rendered this:", attachments=json_block)
