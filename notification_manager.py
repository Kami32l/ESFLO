import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("C:\\Users\\T430\\python\\EnvironmentVariables\\.env")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")


class NotificationManager:
    """
    This class is responsible for sending SMS notifications using Twillio API.
    """
    def __init__(self):
        pass

    def send_sms(self, message_text):
        """
        Sends sms with given text using kiwi API.
        :param message_text: text of the message
        """
        print("Message text:", message_text)
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=message_text,
            from_=TWILIO_PHONE_NUMBER,
            to=PHONE_NUMBER,
        )

        print("Message sid:", message.sid)
