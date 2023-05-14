import random
from django.conf import settings
from sms import send_sms, Message
from twilio.rest import Client
from decouple import config
from django.core.mail import EmailMessage


def send_otp(phone_number):
    try:
        otp = random.randint(1000, 9999)
        

        # account_sid = config('account_sid')
        # auth_token = config('auth_token')
        # client = Client(account_sid, auth_token)

        # message = client.messages.create(
        # from_=config('us_phone'),
        # body=otp,
        # to=phone_number
        # )

        return otp

    except Exception as e:
        return None


def send_email(name, email, otp):

    title = 'BuyMoreMart account activation'
    # body = render_to_string('email.html',
    #                         {"user":name,
    #                          "domain":current,
    #                         "otp": otp
    #                          })

    body = str(otp)

    e = EmailMessage(subject=title, body=body, from_email=settings.EMAIL_HOST_USER, to=[email])
    e.send()
    return
