import json
import requests
import os
from access_token import access_token
from other_ids import org_id, department_id


class WocTickets:
    def __init__(self):
        data = {}
        # Set the API endpoint URL
        url = 'https://desk.zoho.com/api/v1/tickets'

        # Set the required headers
        headers = {
            'orgId': org_id,
            'Authorization': f'Zoho-oauthtoken {access_token}'
        }

        # Set the query parameters
        params = {
            'departmentId': department_id,
            'status': 'Open',
            'include': 'contacts,assignee,departments,team,isRead',
            'limit': 50
        }

        # Initialize next_page to None
        next_page = None

        # Initialize a variable to keep track of the number of printed tickets
        num_printed_tickets = 0

        # Loop until all pages have been retrieved
        while True:
            # Make the GET request and store the response
            response = requests.get(url, headers=headers, params=params)

            # Check if the request was successful
            if response.status_code == 200:
                # Extract required information from each ticket
                for ticket in response.json()['data']:
                    ticket_id = ticket['id']
                    email = ticket['email']
                    ticket_number = ticket['ticketNumber']
                    status = ticket['status']
                    status_type = ticket['statusType']
                    modified_time = ticket.get('modifiedTime', 'Key not found')

                    # Print the extracted information
                    print(f"Ticket Number: {ticket_number}")
                    # Print the extracted information
                    # print(f"Ticket ID: {ticket_id}")
                    # print(f"Email: {email}")
                    # print(f"Status: {status}")
                    # print(f"Status Type: {status_type}")
                    print(f"Modified date: {modified_time}")

                    # Store the extracted information in a dictionary
                    new_data = {
                        ticket_id: {
                            "Email": email,
                            "Ticket Number": ticket_number,
                            "Status": status,
                            "Status Type": status_type,
                            "Modified Date": modified_time
                        }
                    }

                    # Add the dictionary to the existing JSON data and save to file
                    try:
                        with open("woc_tickets.json", "r") as woc_tickets:
                            data = json.load(woc_tickets)
                    except FileNotFoundError:
                        pass
                    data.update(new_data)
                    with open("woc_tickets.json", "w") as woc_tickets:
                        json.dump(data, woc_tickets, indent=4)

                    # Increment the counter of printed tickets
                    num_printed_tickets += 1

                # Check if there are more pages of data
                if next_page:
                    params['page'] = next_page
                else:
                    break  # All pages have been retrieved

                # Get the next page of data
                next_page = None
                if 'info' in response.json():
                    next_page = response.json()['info']['next_page']
            else:
                # Print the error message
                print('Error:', response.status_code, response.text)
                break

        # Print the number of printed tickets after the loop has finished executing
        print(f"Number of printed tickets: {num_printed_tickets}")

        try:
            os.remove("woc_tickets.json")
        except FileNotFoundError:
            pass
        with open("woc_tickets.json", "w") as woc_tickets:
            json.dump(data, woc_tickets, indent=4)
