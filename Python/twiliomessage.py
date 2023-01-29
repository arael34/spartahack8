def check_temp(temp):
    account_sid_v, auth_token, twilio_number, target_number = '', '', '', ''

    with open('tokens.txt', 'r') as tokenfile:
        lines = [line.rstrip('\n') for line in tokenfile]
        try:
            account_sid_v, auth_token, twilio_number, target_number = lines[0], lines[1], lines[2], lines[3]
        except:
            print('Error: Invalid tokens.txt format!')
            return

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
    # TODO
    # target_number = changed_value # change .txt file
    print('target number has changed')
