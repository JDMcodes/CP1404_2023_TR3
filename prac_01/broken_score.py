"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


while True:
    try:
        # validate that a number is input as a score
        score = float(input("Enter score: "))
    except ValueError:
        print("Invalid score, please enter a number from 0 to 100")
    else:
        # check that it is within the required range
        if 0 <= score <= 100:
            break
        else:
            print("Invalid score, please enter a number from 0 to 100")

# generate feedback for score
if score > 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
