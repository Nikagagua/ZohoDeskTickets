import requests
import json
from access_token import access_token
from other_ids import department_id


class CreateTickets:
    def __init__(self):
        self.url = "https://desk.zoho.com/api/v1/tickets"

        self.payload = json.dumps({
            "subject": "Testing Automation",
            "description": "Automation test",
            "departmentId": department_id,
            "contact": {
                "firstName": "S2S",
                "lastName": "Testing",
                "email": "s2stesting@hotmail.com"
            },
            "channel": "Email",
            "classification": "Feature"
        })

        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}',
        }

        self.response = requests.request("POST", self.url, headers=self.headers, data=self.payload)

        print(self.response.text)

        if self.response.status_code == 200:
            print("Ticket created successfully")
        else:
            print("Error creating ticket")
