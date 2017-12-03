# import json
import re

from slackbot import bot

from . import utils


@bot.respond_to('show balance[s]?', flags=re.IGNORECASE)
def balances(message):
    """
    :param message: command to initiate balance report
    :return: an attachment with summary of account status
    """
    account_info = utils.get_account_info()
    accounts = utils.template_data_account_info(account_info)

    message.reply_webapi(
        "Accounts Balances",
        attachments=utils.j2_env.get_template('account_info').render(**{'accounts': accounts}))
