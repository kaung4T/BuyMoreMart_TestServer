# from twilio.rest import Client
# from decouple import config

# account_sid = config('account_sid')
# auth_token = config('auth_token')
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_=config('us_phone'),
#   body='hello',
#   to='+959455033077'
# )

# print(message.sid)

def check_phone_num (phone_number):
    phone = phone_number
    new = "+959"
    position = 0


    if phone[0] == "0" and phone[1] == "9":
        while position < len(phone):
            if position != 0 and position != 1:
                new += phone[position]
            position += 1
    else:
        for phone_one in phone:
            new += phone_one

    if phone[0] == "+" and phone[1] == "9" and phone[2] == "5" and phone[3] == "9":
        new = phone
  
    return new

print(check_phone_num("9595033077"))
