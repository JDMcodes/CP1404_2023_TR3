"""
CP1404
Taxi class TEST

estimate: 30 min
actual: 30min
"""

from taxi import Taxi


def main():
    """Taxi class TEST"""
    my_taxi = Taxi("hummer", 100)
    my_taxi.drive(40)
    fare = my_taxi.get_fare()
    print(fare)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    fare = my_taxi.get_fare()
    print(fare)
    print(my_taxi)

main()


