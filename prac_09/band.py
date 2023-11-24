"""Band class for CP1404

estimate: 30min
actual: "40min"
"""

class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name."""
        self.name = name
        self.members = []


    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.members})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, member):
        """Add a Musician to the band."""
        self.members.append(member)

    def play(self):
        """prints a set of strings showing what the members are playing"""
        for member in self.members:
            if not member.instruments:
                print(f"{member.name} needs an instrument!")
            else:
                print(f"{member.name} is playing: {member.instruments[0]}")



