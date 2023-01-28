account_sid_v = 'AC536d3cc75c7b11f0ee561f4d7d0d3057'
auth_token = 'bf3d9c39e09188676c9705700d595eb2'
twilio_number = '+18446506305'
target_number = '+15179803378'

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

def change_number(changed_value):
    target_number = changed_value
    print('target number has changed')
