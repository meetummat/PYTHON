# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

from random import randint
# Here we directly imported randint from the random module.
# "from" is a keyword in Python, so it cannot be used as a variable name.


class Train:
    def __init__(self, trainNo):
        # We can change the name of the self parameter to any valid name,
        # but using "self" is the standard practice and is better for readability.
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked from train number {self.trainNo}, from {fro} to {to}")

    def getStatus(self):
        print(f"Train number {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(
            f"Ticket fare in train number {self.trainNo}, "
            f"from {fro} to {to} is {randint(222, 5555)}"
        )


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")