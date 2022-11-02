import os
import json
from sendgrid import SendGridAPIClient

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

def pretty_print(data):
    parsed = json.loads(data.body)
    return print(json.dumps(parsed, indent=4, sort_keys=True))

def get_lists():
    response = sg.client.marketing.lists.get()
    pretty_print(response)

def get_list(id):
    response = sg.client.marketing.lists._(id).get()
    pretty_print(response)
    response = sg.client.marketing.contacts.get()
    pretty_print(response)

def create_list(name):
    data = {"name": name}
    response = sg.client.marketing.lists.post(
        request_body=data
    )
    pretty_print(response)
    parsed = json.loads(response.body)
    return parsed['id']

def update_list(name, list_id):
    id = list_id
    data = {"name": name}
    response = sg.client.marketing.lists._(id).patch(
        request_body=data
    )
    pretty_print(response)

def add_contact_to_list(email, list_id):
    data = {
        "list_ids": [list_id],
        "contacts": [{"email": email}]
    }
    response = sg.client.marketing.contacts.put(request_body=data)
    pretty_print(response)

def delete_list(list_id):
    response = sg.client.marketing.lists._(list_id).delete()
    print(response.status_code)

def delete_all_contacts():
    params = {"delete_all_contacts": "true"}
    response = sg.client.marketing.contacts.delete(
        query_params=params
    )
    print(response.status_code)

# create_list("On-Demand Superclass 2022 - Clicked Links")