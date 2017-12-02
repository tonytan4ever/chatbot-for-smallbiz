'''
utils function for slackbot
'''

from slackbot import settings


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
