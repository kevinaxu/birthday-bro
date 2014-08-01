# Checks the data file for any birthdays today. If there are, 
#	constructs and sends the text through Twilio api. 
from twilio.rest import TwilioRestClient

# Check the data file for any birthdays. Returns a list of 
#	birthdays if available. 
def find_birthdays(): 
	return true

# Constructs the text for each number given a number of standard
#	birthday templates 
def construct_texts(): 
	return true 

# Sends the actual texts out using Twilio API 
def send_sms():

	account_sid = "AC5ef8732a3c49700934481addd5ce1659"
	auth_token  = "{{ auth_token }}"
	client = TwilioRestClient(account_sid, auth_token)

	sms = client.sms.messages.create(body="Jenny please?! I love you <3",
			to="+14159352345", from_="+14158141829")
	print sms.sid

