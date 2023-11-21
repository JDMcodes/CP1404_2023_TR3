"""CP1404 Practical - Guitar Class & Program

Guitar Class
Estimate: 30min
Actual: 25min
"""


class Guitar:
    """Represent a Guitar Class object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.
        """
        self.name = name
        self.year = year
        self.cost = cost
        self.age = self.get_age()

    def __str__(self):
        """Returns a string describing the Guitar Object"""
        return f"{self.name}({self.year}): ${self.cost}"

    def get_age(self):
        """Determines Guitars Age"""
        age = 2023 - self.year
        return age

    def is_vintage(self):
        """Determines whether the Guitar is Vintage or not"""
        if self.age >= 50:
            vintage = True
        else:
            vintage = False
        return vintage



