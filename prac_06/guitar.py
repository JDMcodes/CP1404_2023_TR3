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

def test_guitar():

    """Program that uses the guitar class to create a list of your guitars and then prints a summary"""

    print("My Guitars!")
    guitar_list = []
    # while len(guitar_list) >= 0:
    #     new_guitar_name = input("Name:")
    #     if new_guitar_name == "":
    #         break
    #     else:
    #         try:
    #             new_guitar_year = int(input("Year:"))
    #         except ValueError:
    #             print("enter a valid number for year")
    #             new_guitar_year = int(input("Year:"))
    #         try:
    #             new_guitar_cost = float(input("Cost:"))
    #         except ValueError:
    #             print("enter a valid number for cost")
    #             new_guitar_cost = float(input("Year:"))
    #         new_guitar = Guitar(new_guitar_name, new_guitar_year, new_guitar_cost)
    #         guitar_list.append(new_guitar)
    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(guitar_list, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

test_guitar()



