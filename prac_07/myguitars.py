"""CP1404 Practical - My Guitar Program

Guitar Class
Estimate: 30min
Actual: 35min
"""

from guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        price = float(parts[2])
        guitar = Guitar(parts[0], year, price)
        guitars.append(guitar)
        print(guitar)
    guitars.sort()



main()
