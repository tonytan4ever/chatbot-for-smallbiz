# import json
import re

from slackbot import bot

from . import utils


@bot.respond_to('Can you transfer (\$?[0-9]+(?:\.[0-9][0-9])?) from (\w+) to (\w+)[\?]?$', flags=re.IGNORECASE)
def transfer(message, amount=None, acc_src=None, acc_dest=None):
    """

    :param message: ex. `Can you transfer $999.99 from Checking to Savings?`
    :param amount: dollar amount parsed from message
    :param acc_src: Source account
    :param acc_dest: Destination account
    :return: status of transfer creation request
    """
    message.send('Initiating transfer ...')

    if not all([amount, acc_src, acc_dest]):
        message.reply("I'm sorry I did not understand your request.")
        return

    # message.reply(', '.join([amount, acc_src, acc_dest]))

    # TODO: build payload for REST API
    # TODO: POST /fundstransfer with payload
    # Reply with result from API

    # resp_json = requests.post(
    #     url, params=params, data=json.dumps(data), headers=headers)

    resp_json = {
        "SetUpComplete": "success"
    }

    if 'SetUpComplete' in resp_json and resp_json["SetUpComplete"] == 'success':
        message.reply(
            "I have successfully completed the transfer: {0}".format(amount))

    message.reply_webapi("Follow up question:",
                         attachments=utils.j2_env.get_template('follow_up_transfer').render())
