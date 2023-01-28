account_sid_v = 'pl'
auth_token = 'pl'
twilio_number = 'pl'
target_number = 'pl'

def check_temp(temp):
    from twilio.rest import Client
    client = Client(account_sid_v, auth_token)
    
    if temp < 0:
        client.messages.create(
            body="This is a temperature warning - your room has reached an abnormally low reading of: " + str(temp),
            from_ = twilio_number,
            to = target_number
        )
        print('cold message sent')
    elif temp > 60:
        client.messages.create(
            body="This is a temperature warning - your room has reached an abnormally high reading of: " + str(temp),
            from_ = twilio_number,
            to = target_number
        )
        print('heat message sent')

import mimetypes
import os
from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

client = Client(account_sid_v, auth_token)

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