# algorithm
# get no. of items
# get price of 1st item
# ...
# get price of nth item
# total cost of all items
# return total cost and number of items
#

# get number of items
while True:
    try:
        # validate that a number is input for number of items
        number_of_items = int(input("How many items are being scanned: "))
        # validate that the number of items is greater than 0
        if number_of_items <= 0:
            print("Invalid entry, please enter a number greater than 0")
            continue
        break
    except ValueError:
        print("Invalid entry, please enter a number greater than 0")

# list to store prices
all_prices = []
# get prices
for i in range(0, number_of_items, 1):
    while True:
        try:
            # validate that a number is input as the price
            price = float(input(f"Enter price for item {(i+1)}: "))
            # validate price is above 0
            if price <= 0:
                print("Price must be greater than 0")
                continue
            # store and return prices
            all_prices.append(price)
            print(f"Price of item {(i + 1)} is ${price:.2f}")
            break
        except ValueError:
            print("Invalid price, price must be a number greater than 0.")

# calculate total and return summary of prices
total_price = sum(all_prices)
if number_of_items == 1:
    print(f"Total price for {number_of_items} item is ${total_price:.2f}")
else:
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")
