from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse

import data_in

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body =  request.values.get('Body').lower()
    msg = ''

    if body == 'temperature':
        msg = 'The current temperature is: ' + str(data_in.latest_temp) + ' C'
    elif body == 'sound':
        msg = 'The current sound level is: ' + str(data_in.latest_soundlevel) + ' dB'
    else:
        msg = 'Unrecognized command. Request either temperature("temperature") or sound level("sound")'

    resp = MessagingResponse()
    resp.message(msg)
    return Response(str(resp))

if __name__ == '__main__':
    app.run(debug=True)
