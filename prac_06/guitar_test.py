"""CP1404 Practical - Guitar Class Test Code
Estimate: 10min
Actual: 15min
"""

from guitar import Guitar

def main():
    """Tests Guitar Class Functions and prints statements for confirmation"""
    fender = Guitar("Fender Stratocaster",2014,765.4)
    gibson = Guitar("Gibson L-5 CES",1922,16035.4)


    print(f"{fender.name} get_age() - expected: 9. got: {fender.get_age()}")
    print(f"{fender.name} is_vintage() - expected: False. got: {fender.is_vintage()}")
    print(f"{gibson.name} get_age() - expected: 9. got: {gibson.get_age()}")
    print(f"{gibson.name} is_vintage() - expected: False. got: {gibson.is_vintage()}")
    print(fender.cost)


main()



