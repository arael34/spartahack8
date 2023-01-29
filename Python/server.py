from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    body =  request.values.get('Body').lower()
    msg = ''

    import pickle
    if body == 'temperature':
        temperature = 0.
        with open("temp.p", "rb") as tempfile:
            temperature = pickle.load(tempfile)
        msg = 'The current temperature is: ' + str(temperature) + ' C'
    elif body == 'sound':
        noise = 0
        with open("noise.p", "rb") as noisefile:
            noise = pickle.load(noisefile)
        msg = 'The current sound level is: ' + str(noise) + ' dB'
    else:
        msg = 'Unrecognized command. Request either temperature("temperature") or sound level("sound")'

    resp = MessagingResponse()
    resp.message(msg)
    return Response(str(resp))

if __name__ == '__main__':
    app.run(debug=True)
