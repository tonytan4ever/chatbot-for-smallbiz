'''
Created on Dec 2, 2017

@author: tonytan4ever
'''
import json
import re

from slackbot import bot


@bot.respond_to("Pay my last invoice$", re.IGNORECASE)
def pay_invoice_handler(message):
    resp = [
        {
            "title": "Fun Game, LLC",
            "text": "Pay Invoice",
            "fallback": "If you could read this message, you'd be choosing something fun to do right now.",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "callback_id": "confirm_invoice_payment",
            "actions": [
                {
                    "name": "yes",
                    "text": "Confirm",
                    "type": "button",
                    "value": True
                },
                {
                    "name": "no",
                    "text": "Nevermind",
                    "type": "button",
                    "value": False
                }
            ]
        }
    ]
    message.reply_webapi("Okay, your next invoice with FunGame LLC is $190.80m, "
                         "Confirm payment ?", 
                         attachments=json.dumps(resp))
