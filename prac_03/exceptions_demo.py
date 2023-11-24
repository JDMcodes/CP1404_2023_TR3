"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the wrong value is assigned, example it doesnt exist or it is invalid for an operation.
2. When will a ZeroDivisionError occur?
When you attempt to divide by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("denominator cannot be zero")
        try:
            denominator = int(input("Enter the denominator: "))
        except ValueError:
            print("Numerator and denominator must be valid numbers!")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")