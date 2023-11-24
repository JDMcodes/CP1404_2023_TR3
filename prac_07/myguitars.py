"""CP1404 Practical - My Guitar Program

Guitar Class
Estimate: 30min
Actual: 35min
"""

from guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    guitar_list = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        price = float(parts[2])
        guitar = Guitar(parts[0], year, price)
        guitar_list.append(guitar)

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
    guitar_list.sort()
    guitar_strings_list = []
    for guitar in guitar_list:
        guitar_strings = f"\n{guitar.name},{guitar.year},{guitar.cost}"
        guitar_strings_list.append(guitar_strings)
    out_file = open('guitars.csv', 'w')
    out_file.writelines(guitar_strings_list)
    out_file.close()

main()
