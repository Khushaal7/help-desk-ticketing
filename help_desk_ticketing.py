Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Ticket:
    ticket_counter = 2001
    total_tickets = 0
    resolved_tickets = 0
    open_tickets = 0

    def __init__(self, staff_id, ticket_creator, contact_email, description):
        Ticket.total_tickets += 1
        Ticket.open_tickets += 1
        self.ticket_number = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.staff_id = staff_id
        self.ticket_creator = ticket_creator
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def submit_ticket(self):
        print("Ticket submitted successfully.")

    def respond_to_ticket(self, response):
        self.response = response
        if "Password Change" in self.description:
            self.generate_new_password()
            self.status = "Closed"
            Ticket.resolved_tickets += 1
            Ticket.open_tickets -= 1
        print("Ticket response added successfully.")

    def resolve_ticket(self):
        self.status = "Closed"
        Ticket.resolved_tickets += 1
        Ticket.open_tickets -= 1
        print("Ticket resolved successfully.")

    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.resolved_tickets -= 1
        Ticket.open_tickets += 1
        print("Ticket reopened successfully.")

    def generate_new_password(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.ticket_creator[:3]
            self.response = f"New password generated: {new_password}"

    def print_stats(self):
        print("Displaying Ticket Statistics")
        print(f"Tickets Created: {Ticket.total_tickets}")
        print(f"Tickets Resolved: {Ticket.resolved_tickets}")
        print(f"Tickets To Solve: {Ticket.open_tickets}")

    def print_ticket_info(self):
        print(f"\nTicket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.ticket_creator}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}")


# Create ticket instances and test the functionality
ticket1 = Ticket("INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working")
ticket1.print_ticket_info()

ticket2 = Ticket("MARIAH", "Maria", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
ticket2.print_ticket_info()

ticket3 = Ticket("JOHNS", "John", "john@whitecliffe.co.nz", "Password change")
ticket3.generate_new_password()
ticket3.print_ticket_info()

print("\nDisplaying Ticket Statistics")
print(f"Tickets Created: {Ticket.total_tickets}")
print(f"Tickets Resolved: {Ticket.resolved_tickets}")
print(f"Tickets To Solve: {Ticket.open_tickets}")

ticket2.respond_to_ticket("The monitor has been replaced.")
ticket2.print_ticket_info()

ticket3.resolve_ticket()
ticket3.print_ticket_info()

ticket2.reopen_ticket()
ticket2.print_ticket_info()

print("\nDisplaying Ticket Statistics")
print(f"Tickets Created: {Ticket.total_tickets}")
print(f"Tickets Resolved: {Ticket.resolved_tickets}")
print(f"Tickets To Solve: {Ticket.open_tickets}")
