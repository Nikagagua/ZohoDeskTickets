import json


class OwnerMails:
    def __init__(self):
        with open("woc_tickets.json", 'r') as woc_ticket_emails:
            ticket_emails = json.load(woc_ticket_emails)
        self.emails = [ticket_info['Email'] for ticket_id, ticket_info in ticket_emails.items()]

        # print(self.emails)
