'''
utils function for slackbot
'''

import json
import os

from jinja2 import Environment, FileSystemLoader
from memcache import Client

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


try:
    CACHE = Client(settings.MEMCACHED_SERVERS)
    CACHE_TTL = settings.MEMCACHED_TTL if settings.MEMCACHED_TTL else 0
except:
    CACHE = None


def cache_get(key):
    """
    Retrieves a value for a given key in cache. Alternatively you can implement
    your own caching here. Caching is optional and should return "None" if
    no caching is enabled.
    :param key: A string representing the key for a given key-value pair
    :return: The value for a given key-value pair. If it doesn't exists
        in cache it returns "None"
    Caching is optional and should return "None" if no caching is enabled
    """
    if CACHE is None:
        return None

    return CACHE.get(key)


def cache_set(key, value, ttl=None):
    """
    Stores a key-value pair in cache.
    Alternatively you can implement your own caching here. Caching is optional
    and this method should return nothing if no caching is enabled
    :param key: A string representing the key for a given key-value pair
    :param value: The value for a given key-value pair
    :param ttl: How long in seconds a key-value pair should live in cache.
        use ttl=0 to cache forever.
    :return: If no cache client is found this method will simply return
    """
    if CACHE is None:
        return
    elif ttl is None:
        ttl = CACHE_TTL

    CACHE.set(key, value, ttl)


def get_account_info():
    with open(
        os.path.join(
            settings.ROOT_DIR,
            'chatbot',
            'user908997180284469041accounts.json')) as json_file:
        data = json.load(json_file)

    cached_account_info = cache_get('account_info')

    if cached_account_info:
        return json.loads(cached_account_info)
    else:
        cache_set('account_info', json.dumps(data))
        return data


def template_data_account_info(account_info):
    accounts = []
    for account in account_info['AccessibleAccountDetailList']:
        account_details = {
            'balance': account['BasicAccountDetail']['Balances']['AvailableBalanceAmount'],
            'acct_type': account['BasicAccountDetail']['Codes']['CategoryDescription'],
            'acct_num': account['BasicAccountDetail']['RedactedAccountNumber']
        }

        accounts.append(account_details)

    return accounts
