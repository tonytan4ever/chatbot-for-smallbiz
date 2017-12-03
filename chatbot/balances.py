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
    resp_json = utils.get_accounts_info()
    accounts = []
    for account in resp_json['AccessibleAccountDetailList']:
        account_details = {
            'balance': account['BasicAccountDetail']['Balances']['AvailableBalanceAmount'],
            'acct_type': account['BasicAccountDetail']['Codes']['CategoryDescription'],
            'acct_num': account['BasicAccountDetail']['RedactedAccountNumber']
        }

        accounts.append(account_details)

    message.reply_webapi(
        "Accounts Balances",
        attachments=utils.j2_env.get_template('account_info').render(**{'accounts': accounts}))
