"""CP1404 Practical - Project Class


Estimate: 30min
Actual:
"""


class Project:
    """Represent a Project Class object."""

    def __init__(self, name="", date="", priority=0, cost=0, percent=0):
        """Initialise a Priority instance.
        """
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.percent = percent

    def __str__(self):
        """Returns a string describing the Project Object"""
        return f"{self.name}, start: {self.date}, priority {self.priority}, estimate: ${self.cost}, completion: {self.percent}%"

    def __lt__(self, other):
        """Returns True if self's priority is
           less than other's priority, and False otherwise"""
        return self.priority < other.priority


    def is_complete(self):
        """Determines whether the Project is Complete or not"""
        if self.percent >= 100:
            complete= True
        else:
            complete = False
        return complete
