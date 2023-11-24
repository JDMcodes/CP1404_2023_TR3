"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "price_list.txt"


def main():
    """Creates a .txt file containing the price changes for each day"""
    price = INITIAL_PRICE
    out_file = open(OUTPUT_FILE, 'w')
    price_change_list = generate_price_changes(price)
    price_change_days = generate_price_change_days(price_change_list)
    for i in range(0, len(price_change_list)):
        print(f"On Day {price_change_days[i]} price is: ${price_change_list[i]:,.2f}", file=out_file)
    out_file.close()


def generate_price_changes(price):
    """Creates list of all price changes"""
    price_change_list = []
    while MIN_PRICE <= price <= MAX_PRICE:
        # generate a random integer of 1 or 2
        # if it's 1, the price increases, otherwise it decreases
        if random.randint(1, 2) == 1:
            # generate a random floating-point number
            # between 0 and MAX_INCREASE
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            # generate a random floating-point number
            # between negative MAX_DECREASE and 0
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        price_change_list.append(price)
    return price_change_list


def generate_price_change_days(price_change_list):
    """creates list of numbered days for price change list"""
    day = 0
    days_list = []
    for price_change in price_change_list:
        day = day+1
        days_list.append(day)
    return days_list


main()
