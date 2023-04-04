import json

test_ticket_id = '169574000043807001'


class TicketIds:
    def __init__(self):
        with open("woc_tickets.json", 'r') as woc_ticket_ids:
            ticket_ids = json.load(woc_ticket_ids)

        self.all_ticket_ids = []
        for ticket_id, ticket_info in ticket_ids.items():
            email = ticket_info['Email']
            self.all_ticket_ids.append(ticket_id)

        # print(self.all_ticket_ids)
