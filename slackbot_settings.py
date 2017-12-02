import logging
import sys


API_TOKEN = "<your_API_token>"

DEFAULT_REPLY = ("I don't know how to help small business when you "
                 "talk like this")

ERRORS_TO = 'chatbot_for_small_biz'

STARTING_MESSAGE = "Starting Chatbot"


DEBUG = True

LOGGING_CONF = {
    'format': '[%(asctime)s] %(message)s',
    'datefmt': '%m/%d/%Y %H:%M:%S',
    'level': logging.DEBUG if DEBUG else logging.INFO,
    'stream': sys.stdout,
}
