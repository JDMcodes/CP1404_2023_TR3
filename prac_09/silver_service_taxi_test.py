"""
CP1404
silver service taxi class TEST

estimate: 30 min
actual: 30min
"""

from silver_service_taxi import SSTaxi


def main():
    """silver service Taxi class TEST"""
    my_taxi = SSTaxi("hummer", 100,2)
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