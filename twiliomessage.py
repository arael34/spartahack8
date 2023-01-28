account_sid_v = 'pl'
auth_token = 'pl'
twilio_number = '+pl'
target_number = '+pl'

temperature = 38

import mimetypes
import os
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

client = Client(account_sid_v, auth_token)

def high_temperature():
    if temperature < 42:
        client.messages.create(
        body="This is a temperature warning - your room has reached an abnormally high reading of: " + str(temperature),
        from_ = twilio_number,
        to = target_number
        )
        return 'temperature message sent'

def change_number(changed_value):
    target_number = changed_value
    print('target number has changed')
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
    body =  request.values.get('Body')
    return str(body)

if __name__ == '__main__':
    app.run(debug=True)