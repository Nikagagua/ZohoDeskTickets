from close_tickets import CloseTickets
from email_reply import EmailReply
from all_woc_tickets import WocTickets
from ticket_owner_emails import OwnerMails
from ticket_id import TicketIds

# woc_tickets = WocTickets()

# //////////////////////////////////////////////////////////////////////////////
# Get emails and send reply to all of them
# Create an instance of OwnerMails to fetch the emails from woc_tickets.json
owner_mails = OwnerMails()
#
# # Create an instance of EmailReply and pass the list of emails to it
email_reply = EmailReply(owner_mails.emails)
#
# # Call the send_replies method to send email replies to all the emails in the list
email_reply.send_replies()
# //////////////////////////////////////////////////////////////////////////////////
# Get ticket Ids and close them at once
ticket_ids = TicketIds().all_ticket_ids
# close_tickets = CloseTickets(ticket_ids)
# ///////////////////////////////////////////////////////////////////////////////////
