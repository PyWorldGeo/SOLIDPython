#1
#The Single Responsibility Principle states that a class should do one thing and
# therefore it should have only a single reason to change.

#To state this principle more technically: Only one potential change
# (database logic, logging logic, and so on.) in the software’s
# specification should be able to affect the specification of the class.

#Incorrect
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_email(self, message):
        # sending an email to the customer
        pass

    def place_order(self, order):
        # placing an order
        pass

    def generate_invoice(self, invoice):
        # generating an invoice
        pass

    def add_feedback(self, feedback):
        # add feedback
        pass

#Correct
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class EmailService:
    def send_email(self, customer, message):
        # Sending an email to the customer
        pass

class OrderService:
    def place_order(self, customer, order):
        # Placing an order
        pass

class InvoiceService:
    def generate_invoice(self, customer, invoice):
        # Generating an invoice
        pass

class FeedbackService:
    def add_feedback(self, customer, feedback):
        # add customer feedback
        pass