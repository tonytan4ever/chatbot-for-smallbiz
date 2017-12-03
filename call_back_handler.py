import json

from flask import Flask, request, jsonify
import requests


clientId = '280860704740.280949647332'
clientSecret = 'fd0ab6493feda3b5efcc78852bd2d6f9'

app = Flask('SlackReceiver')


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


@app.route('/slack/message', methods=['POST'])
def incoming_slack_message():
    req = request.get_json()
    print req
    # .. do something with the req ..
    return 'action successful'


@app.route('/slack/options', methods=['POST', 'OPTIONS'])
def incoming_slack_options():
    # .. idk ..
    return 'ok'


@app.route('/command', methods=['POST'])
def incoming_command():
    return 'Your ngrok tunnel is up and running!'


if __name__ == '__main__':
    app.run(debug=True)
