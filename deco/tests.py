from django.test import TestCase
from twilio.rest import Client


# Create your tests here.
phone = '+918888334844'

'''q = way2sms.sms('8888334844', 'G4592C')
q.send('8888334844', 'aditya')
n = q.msgSentToday()
q.logout()'''

account_sid = 'AC34ee859c1832745012adc68428d840a6'
auth_token = '153888f2fca0da540e9deb290f692fda'
client = Client(account_sid, auth_token)
message = client.messages.create(
 body='This is a test message! by aditya',
 from_='[+][120][28167190]',
 to=phone
 )

