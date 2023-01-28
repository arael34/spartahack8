account_sid_v = 'AC536d3cc75c7b11f0ee561f4d7d0d3057'
auth_token = 'bf3d9c39e09188676c9705700d595eb2'
twilio_number = '+18446506305'
target_number = '+15179803378'

temperature = 38

from twilio.rest import Client

client = Client(account_sid_v, auth_token)

def high_temperature():
    if temperature < 42:
        client.messages.create(
        body="This is a temperature warning - your room has reached an abnormally high reading of: " + str(temperature),
        from_ = twilio_number,
        to = target_number
        )
        print('temperature message sent')

def change_number(changed_value):
    target_number = changed_value
    print('target number has changed')
