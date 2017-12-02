'''
utils function for slackbot
'''

import json
import os

from jinja2 import Environment, FileSystemLoader

from slackbot import settings


j2_env = Environment(
    loader=FileSystemLoader(os.path.join(settings.BOT_ROOT_DIR, 'chatbot', 'templates')),
    trim_blocks=True
)


def get_user_name_from_message(message):
    users = message._client.users
    userid = message._get_user_id()
    return users[userid]['name']


def direct_reply_to_message(message, text):
    channel_id = _open_n_get_message_channel_id(message)
    message._client.rtm_send_message(channel_id, text)


def _open_n_get_message_channel_id(message):
    return (message._client.webapi.im.open(message._get_user_id()).
            body['channel']['id'])


def get_accounts_info():
    with open('/home/isaac/PycharmProjects/chatbot-for-smallbiz/user908997180284469041accounts.json') as json_file:
        data = json.load(json_file)

    return data
