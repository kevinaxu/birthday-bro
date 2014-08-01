# Runs every Monday at 9:00. Looks up the birthdays for the following week
# week (next Monday to next next Monday). Sends a message containing 
# person [nick]name, number, and text to send. Gives the user a chance to 
# remove the person from the list if the birthday text is unwarranted 
from twilio.rest import TwilioRestClient

def main(): 
	all_birthdays = find_future_birthdays()
	send_email(all_birthdays): 

def find_future_birthdays(): 
	return true 

def find_past_messages(): 
	ACCOUNT_SID = "AC9fccdd061492e537e2b786bf92a11496" 
	AUTH_TOKEN = "[AuthToken]" 
	 
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	  
	messages = client.messages.list() 
	for m in messages: 
		print m.sid

# Uses Mandrill API to send an email digest of the texts to send 
# Returns true if send was successful, false otherwise 
def send_email: 
	try: 
		mandrill_client = mandrill.Mandrill('jKSORN8NdMzr2upmSJ7Q7A')
		message = {
			'from_email':	'kevinxu16@gmail.com',
			'from_name':	'Birthday Bot', 
			'subject':		"next week's birthday texts!", 
			'text':			'Example text content',
			'to':			[{'email': 'recipient.email@example.com',
								'name': 'Recipient Name',
							'type': 'to'}],
		result = mandrill_client.messages.send(message=message) 

	except mandrill.Error, e:
		print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
		raise

	return true

if __name__=='__main__':main() 

