from twilio.rest import Client
import time
import random
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token  = ""
#Instantiate class TwilioRestClient with your credentials
client = Client(account_sid, auth_token)
twilio_number = "+1"
 
lyrics = open("despacito.txt", "r").readlines()

count = 0

for line in lyrics:
    payload = line.replace("\n","")
    message = client.api.account.messages.create(
        body=payload,
        to="+1",
        from_=twilio_number)
    count += 1
    n = random.randrange(90,300)
    print(str(count)+'-'+str(n))
    time.sleep(n)
