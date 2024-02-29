#4
# Segregation means keeping things separated,
# and the Interface Segregation Principle is about separating the interfaces.
#
# The principle states that many client-specific interfaces are better than one general-purpose
# interface. Clients should not be forced to implement a function they do no need.

#Correct
class Printable:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class Document(Printable):
    def print(self):
        print("Printing document...")

class MultifunctionalDevice(Printable, Scanner):

    def print(self):
        print("Printing document...")

    def scan(self):
        print("Scanning document...")