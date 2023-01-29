from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
from data_in import get_temp #, get_soundlevel

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body =  request.values.get('Body').lower()
    msg = ''

    if body == 'temperature':
        msg = str(get_temp)
    # elif body == 'sound':
    #     msg = 'TODO: sound level'
    else:
        msg = 'Unrecognized command. Request either temperature("temperature") or sound level("sound")'
    
    resp = MessagingResponse()
    resp.message(msg)
    return Response(resp)

if __name__ == '__main__':
    app.run(debug=True)
