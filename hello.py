from twilio.rest import Client 
 
account_sid = 'ACe27cf670a2545c290f01cdce6d0a6e9e' 
auth_token = 'f0c4322715d34cc8bc0e1168e546d396' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello! This is an editable text message. You are free to change it and write whatever you like.',      
                              to='whatsapp:+919359184123' 
                          ) 
 
print(message.sid)