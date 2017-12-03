import json
import os

from flask import Flask, request, jsonify, render_template
import requests
from slackclient import SlackClient

import slackbot_settings

from chatbot import utils

clientId = '280860704740.280949647332'
clientSecret = 'fd0ab6493feda3b5efcc78852bd2d6f9'
# Your app's Slack bot user token
SLACK_BOT_TOKEN = "xoxb-280393686641-LnEasPmM6cJrWLMQYNHwGL64"

# Slack client for Web API requests
slack_client = SlackClient(SLACK_BOT_TOKEN)

app = Flask('SlackReceiver', template_folder=os.path.join(
        slackbot_settings.ROOT_DIR,
        'chatbot',
        'templates'
    ))


@app.route('/')
def index():
    return "Ngrok is working! Path Hit: " + request.url


@app.route('/oauth')
def oauth_handler():
    code = request.args.get("code")
    if not code:
        return jsonify({"Error": "Looks like we\'re not getting code."}), 500
    else:
        resp = requests.get('https://slack.com/api/oauth.access',
                             params={
                                 'code': code,
                                 'client_id': clientId,
                                 'client_secret': clientSecret
                            })
        return resp.text


@app.route('/events', methods=['POST'])
def handle_events():
    body = request.json
    if body['type'] == 'url_verification':
        challenge = request.json.get(u'challenge')
        return challenge
    elif body['type'] == 'event_callback':
        if body['event']['user'] != "U88BKL6JV":
            slack_client.api_call(
              "chat.postMessage",
              channel=body['event']['channel'],
              text="Hello, My name is Charles, and I help get your business affairs in order. By connecting your business card accounts, I am able to remind you, pay bills and invoices, and tell you a bunch of business things. Just try it, connect your Visa bank account by entering in the card information",
              attachments=render_template('account_add')
            )

        return "%s joined..." % body['event']['user']
    else:
        return jsonify({"Error": "Unknown event type"}), 500


@app.route('/slack/message', methods=['POST'])
def incoming_slack_message():
    payload = json.loads(request.form['payload'])
    callback_id = payload['callback_id']
    channel = payload['channel']['id']
    if callback_id == 'wopr_bank':
        if payload['actions'][0]['value'] == 'add':
            slack_client.api_call(
                 "chat.postMessage",
                 channel=channel,
                 text='Follow up question',
                 attachments=render_template('another_account')
            )
        return 'Perfect, I added Bilal\'s business account'
    elif callback_id == 'wopr_bank_2':
        if payload['actions'][0]['value'] == 'no':
            slack_client.api_call(
                 "chat.postMessage",
                 channel=channel,
                 text='Follow up question',
                 attachments=render_template('main_menu')
            )

        return 'Great, here are some suggestions how I can assist'
    elif callback_id == 'confirm_invoice_payment':
        if payload['actions'][0]['value']:
            total_cost = 2007.01
            utils.pay_last_invoice(total_cost)
            return 'Fun Game LLC invoice was paid. Your remaining balance is 2007.01'
        else:
            return "Okay, skip paying for now"
    elif callback_id == 'schedule_visa_payment':
        if payload['actions'][0]['value']:
            slack_client.api_call(
                 "chat.postMessage",
                 channel=channel,
                 text='Here are more suggestions how I can assist',
                 attachments=render_template('main_menu')
            )
            return 'All done. Visa payment has been scheduled'
        else:
            slack_client.api_call(
                 "chat.postMessage",
                 channel=channel,
                 text='You good? Or is there any thing else I can help you with?',
                 attachments=render_template('follow_up_schedule_payment')
            )
            return "Okay"
    else:
        return "Error", 500


@app.route('/slack/options', methods=['POST', 'OPTIONS'])
def incoming_slack_options():
    # .. idk ..
    return 'ok'


@app.route('/command', methods=['POST'])
def incoming_command():
    return 'Your ngrok tunnel is up and running!'


if __name__ == '__main__':
    app.run(debug=True)
