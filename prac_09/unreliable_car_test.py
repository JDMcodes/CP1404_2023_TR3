"""
CP1404
Taxi class

estimate: 30 min
actual: 20min
"""

from unreliable_car import UnreliableCar

def main():
    my_car = UnreliableCar("Falcon", 100, 60.02)
    print(my_car)
    distance_drive = my_car.drive(20)
    print(my_car)
    print(distance_drive)

main()

