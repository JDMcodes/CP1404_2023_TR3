# for loop to display all odd numbers from 1 to 21

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# loop to count 10s from 0 to 100

for i in range(0, 110, 10):
    print(i, end=' ')
print()

# count down from 20 to 1
for i in reversed(range(1, 21, 1)):
    print(i, end=' ')
print()

# print n stars

while True:
    try:
        # validate that a number is input for stars
        number_of_stars = int(input("Enter the number of stars: "))
        break
    except ValueError:
        print("Invalid entry, please enter a number")

for i in range(0, number_of_stars, 1):
    print('*', end='')
print()

# print n lines of increasing stars

while True:
    try:
        # validate that a number is input for stars
        number_of_stars = int(input("Enter the number of stars: "))
        break
    except ValueError:
        print("Invalid entry, please enter a number")

for i in range(0, number_of_stars, 1):
    for j in range(0, i+1):
        print('*', end='')
    print()
