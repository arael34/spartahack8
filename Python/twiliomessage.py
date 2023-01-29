"""
To use the twilio API a account SID, auth token, twilio phone number,
and target number must be defined in a "tokens.txt" file, each on a separate
line and in that order. 
ex. tokens.txt
{account SID}
{auth token}
+1 {twilio phone number}
+1 {target phone number}
"""
def check_temp(temp):
    account_sid_v, auth_token, twilio_number, target_number = '', '', '', ''

    with open('tokens.txt', 'r') as tokenfile:
        lines = [line.rstrip('\n') for line in tokenfile]
        try:
            account_sid_v, auth_token, twilio_number, target_number = lines[0], lines[1], lines[2], lines[3]
        except:
            print('Error: Invalid tokens.txt format!')
            return

    import time
    from twilio.rest import Client
    client = Client(account_sid_v, auth_token)

    if temp < 0:
        client.messages.create(
            body="This is a temperature warning - your room has reached an abnormally low reading of: " + str(temp),
            from_ = twilio_number,
            to = target_number
        )
        print('cold message sent')
        time.sleep(60)
    elif temp > 60:
        client.messages.create(
            body="This is a temperature warning - your room has reached an abnormally high reading of: " + str(temp),
            from_ = twilio_number,
            to = target_number
        )
        print('heat message sent')
        time.sleep(60)

def change_number(changed_value):
    lines = []
    with open('tokens.txt', 'r') as tokenfile:
        lines = tokenfile.readlines()
    lines[3] = changed_value + '\n'
    with open('tokens.txt', 'w') as tokenfile:
        tokenfile.writelines(lines)
    print('target number has changed')
