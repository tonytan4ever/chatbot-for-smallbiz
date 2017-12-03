'''
Created on Dec 3, 2017

@author: tonytan4ever
'''
from slackbot import bot

from . import utils


@bot.respond_to("enroll me please$")
def enroll_user(message):
    message.reply_webapi(
    "Hello, My name is Charles, and I help get your business affairs in order."
    "By connecting your business card accounts, I am able to remind you, pay bills and invoices,"
    "and tell you a bunch of business things. Just try it, connect your Visa bank account by entering in the card information",
    attachments=utils.j2_env.get_template('account_add').render())