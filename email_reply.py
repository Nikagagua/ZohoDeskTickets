import requests
import json
from access_token import access_token
from other_ids import org_id
from ticket_id import TicketIds


class EmailReply:
    def __init__(self, emails):
        self.reply_text = f'Dear Customer,\n\n' \
                          ' As we have not heard back from you for a long time, ' \
                          'we will close your support ticket for now.\n' \
                          ' If you would like to reopen the ticket, simply respond to this e-mail. ' \
                          '\n'' This will reopen the ticket automatically, ' \
                          'and one of our agents will get in touch with you.\n\n' \
                          'Best Regards, \n' \
                          'Solutions2Share Support Team'

        self.emails = emails
        self.sent_ticket_ids = []  # keep track of ticket IDs that have already been sent a reply to

    def send_replies(self):
        for email in self.emails:
            for ticket_id in TicketIds().all_ticket_ids:
                if ticket_id in self.sent_ticket_ids:
                    # print(f"Skipping ticket ID {ticket_id} as a reply has already been sent.")
                    continue

                send_reply_payload = {
                    "channel": "EMAIL",
                    "to": email,
                    "fromEmailAddress": "support@solutions2Share.com",
                    "contentType": "plainText",
                    "content": self.reply_text,
                }
                send_reply_headers = {
                    "Content-Type": "application/json",
                    "orgId": org_id,
                    "Authorization": f"Zoho-oauthtoken {access_token}"
                }

                send_reply_url = f"https://desk.zoho.com/api/v1/tickets/{ticket_id}/sendReply"

                response = requests.post(send_reply_url, headers=send_reply_headers,
                                         data=json.dumps(send_reply_payload))

                if response.status_code == 200:
                    print(f"Reply sent to {email} for ticket ID {ticket_id} successfully.")
                    self.sent_ticket_ids.append(ticket_id)  # add the ticket ID to the list
                else:
                    print(
                        f"Failed to send reply to {email} for ticket ID {ticket_id}. "
                        f"Status code: {response.status_code}")

