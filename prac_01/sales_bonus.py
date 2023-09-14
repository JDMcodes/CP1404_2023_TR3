"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# Create list to store all bonuses and sales for future use or validation

bonuses = []
sales = []

# indexes for lists
i = 0

# loop to satisfy algorithm:
# get sales
# while sales >= 0
#     calculate bonus
#     get sales
# do next thing


sale = sales.append(float(input("Enter sale: $")))
while sales[i] >= 0:
    if sales[i] < 1000:
        bonus = sales[i] * 0.1
        print(f"Bonus for this sale: ${bonus:.2f}")
        bonuses.append(bonus)
        i = i + 1
        # # validation
        # print(i)
        # print(bonuses)
    else:
        bonus = sales[i] * 0.15
        print(f"Bonus for this sale: ${bonus:.2f}")
        bonuses.append(bonus)
        i = i + 1
        # # validation
        # print(i)
        # print(bonuses)
    sales.append(float(input("Enter sales: $")))
del sales[i]
total_sales = sum(sales)
total_bonuses = sum(bonuses)
print(f"Total Sales:${total_sales:.2f}")
print(f"Total Bonuses:${total_bonuses:.2f}")

# # validate storage of data
# print(sales)
# print(bonuses)
