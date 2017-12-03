import logging
import os
import sys


API_TOKEN = "xoxb-280393686641-LnEasPmM6cJrWLMQYNHwGL64"

DEFAULT_REPLY = ("I don't know how to help small business when you "
                 "talk like this")

ERRORS_TO = 'chatbot_for_small_biz'

STARTING_MESSAGE = "Starting Chatbot..."

PLUGINS = [
    'chatbot.pay_invoices',
    'chatbot.balances',
    'chatbot.transfer',
    'chatbot.misc',
]

BOT_ROOT_DIR = os.path.dirname(__file__)

DEBUG = True

LOGGING_CONF = {
    'format': '[%(asctime)s] %(message)s',
    'datefmt': '%m/%d/%Y %H:%M:%S',
    'level': logging.DEBUG if DEBUG else logging.INFO,
    'stream': sys.stdout,
}

ROOT_DIR = os.path.dirname(__file__)

MEMCACHED_SERVERS = ['localhost:11211']
MEMCACHED_TTL = 60
