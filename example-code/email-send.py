import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("emaildemo@example.com") # Replace
to_email = To("emaildemo@example.com") # Replace
subject = "Sending with SendGrid is Fun at Superclass"
content = Content("text/html", "Please click <a href=\"https://twilio.com\">here<a> to learn more.")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
