import os
import json
from sendgrid import SendGridAPIClient

sg = SendGridAPIClient(os.environ.get('SENDGRID_EMAIL_VALIDATION_API_KEY'))

data = { "email": "invalid@xyz.com" }
response = sg.client.validations.email.post(request_body=data)
parsed = json.loads(response.body)
print(json.dumps(parsed, indent=4, sort_keys=True))
