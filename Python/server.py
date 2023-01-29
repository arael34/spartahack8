from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
from data_in import get_temp, get_soundlevel

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body =  request.values.get('Body').lower()
    msg = ''

    if body == 'temperature':
        msg = 'The current temperature is: ' + str(get_temp()) + ' C'
    elif body == 'sound':
        msg = 'The current sound level is: ' + str(get_soundlevel()) + ' dB'
    else:
        msg = 'Unrecognized command. Request either temperature("temperature") or sound level("sound")'

    resp = MessagingResponse()
    resp.message(msg)
    return Response(str(resp))

if __name__ == '__main__':
    app.run(debug=True)
