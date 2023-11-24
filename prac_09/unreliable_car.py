"""
CP1404
Taxi class

estimate: 30 min
actual:
"""
import random
from car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability"""
    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car class, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but can fail and only drive 0 if a random number is under its reliability"""
        random_number = 100*random.random()
        print(random_number)
        if random_number <= self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
