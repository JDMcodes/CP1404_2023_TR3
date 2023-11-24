"""CP1404 Practical - Programming Language Class
Estimate: 60min
Actual: 20min
"""


class ProgrammingLanguage:
    """Represent a Program Language Class object."""

    def __init__(self, name, typing="Static", reflection="Yes", year=1990):
        """Initialise a Programming Language instance.
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns a string describing the Programming Language Object"""
        return f'{self.name}, {self.typing}, reflection = {self.reflection}, first appeared in {self.year}'

    def is_dynamic(self):
        """Determines whether the Programming Language is dynamically typed or not"""
        if self.typing.upper() == "DYNAMIC":
            return True
        else:
            return False



