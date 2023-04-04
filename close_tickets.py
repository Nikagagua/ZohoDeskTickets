import requests
import json
from access_token import access_token


class CloseTickets:
    def __init__(self, ticket_ids):
        self.close_url = "https://desk.zoho.com/api/v1/closeTickets"
        self.close_headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}',
        }

        close_payloads = []
        for ticket_id in ticket_ids:
            close_payloads.append({
                "ids": [
                    ticket_id
                ]
            })

        for close_payload in close_payloads:
            close_response = requests.request("POST", self.close_url, headers=self.close_headers,
                                              data=json.dumps(close_payload))

            if close_response.status_code == 200:
                print(f"Closed ticket {ticket_id} successfully")
            else:
                print(f"Error closing ticket {ticket_id}")
