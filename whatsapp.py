
#1.twilio client setup
#2.user input 
#3.scheduling logic
#4.send message
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# 1. Twilio credentials
account_sid = 'twilio_id'
auth_token = 'account_auth'
client = Client(account_sid, auth_token)

# 2. Function to send WhatsApp messages
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred: {e}')

# 3. User input
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g., +12345): ')
message_body = input('Enter the message you want to send: ')

# 4. Schedule input
date_str = input('Enter date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send message (HH:MM in 24hr format): ')

#  Correct conversion: parse the string into a datetime object
scheduled_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")

current_datetime = datetime.now()
time_difference = scheduled_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print(' The specified time is in the past. Please enter a future date and time.')
else:
    print(f' Message to be sent to {name} at {scheduled_datetime}. Waiting...')
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number, message_body)
