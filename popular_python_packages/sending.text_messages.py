# learn how to send a text messages while using twilio.
# twilio: is very popular communication platform for adding voice, video and messaging to your applications.

from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)
try:
    client.messages.create(
        to= config.my_number,
        from_= config.phone_number,
        body="Hello Omar"
    )
except Exception as e:
    print(f"Faild to send message: {e}")