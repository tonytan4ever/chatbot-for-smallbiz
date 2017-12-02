# import json
import re

from slackbot import bot

from . import utils


@bot.respond_to('show balance[s]?', flags=re.IGNORECASE)
def balances(message):
    # TODO get bank accounts for a single user
    # TODO get balances for all bank accounts for that user
    # TODO format response as attachment in slack

    resp_json = utils.get_accounts_info()
    accounts = []
    for account in resp_json['AccessibleAccountDetailList']:
        account_details = {
            'balance': account['BasicAccountDetail']['Balances']['AvailableBalanceAmount'],
            'acct_type': account['BasicAccountDetail']['Codes']['CategoryDescription'],
            'acct_num': account['BasicAccountDetail']['RedactedAccountNumber']
        }

        accounts.append(account_details)

    import pdb; pdb.set_trace()
    message.reply_webapi(
        "Accounts Info",
        attachments=utils.j2_env.get_template('account_info').render(**{'accounts': accounts}))
