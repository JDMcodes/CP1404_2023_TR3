"""CP1404 Practical - Guitar Program

estimate:45min
actual: 40min
"""

from guitar import Guitar
def main():
    """Program that uses the guitar class to create a list of your guitars and then prints a summary"""

    print("My Guitars!")
    guitar_list = []
    while len(guitar_list) >= 0:
        new_guitar_name = input("Name:")
        if new_guitar_name == "":
            break
        else:
            try:
                new_guitar_year = int(input("Year:"))
            except ValueError:
                print("enter a valid number for year")
                new_guitar_year = int(input("Year:"))
            try:
                new_guitar_cost = float(input("Cost:"))
            except ValueError:
                print("enter a valid number for cost")
                new_guitar_cost = float(input("Year:"))
            new_guitar = Guitar(new_guitar_name, new_guitar_year, new_guitar_cost)
            guitar_list.append(new_guitar)

    for i, guitar in enumerate(guitar_list, 1):
        if guitar.is_vintage():
            vintage_string = " (vintage)"
        else:
            vintage_string = ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
main()