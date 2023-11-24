"""
CP1404
silver service taxi class

estimate: 30 min
actual: 45min

"""
from taxi import Taxi


class SSTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km*fanciness
        self.flagfall = 4.50
    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        # round fare result to nearest 10c
        fare = round(self.price_per_km * self.current_fare_distance, 1) + self.flagfall
        return fare

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven