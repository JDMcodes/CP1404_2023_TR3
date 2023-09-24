"""

Temperature converter with functions.
"""


def main():
    """Converts temperature based on a user selection from a menu"""
    temperature_unit = get_temperature_unit()
    if temperature_unit == "F":
        convert_f_to_c()
    elif temperature_unit == "C":
        convert_c_to_f()
    else:
        print("Thank you")


def get_temperature_unit():
    """Gets user input from menu."""
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "C" and choice != "F" and choice != "Q":
        print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    return choice


def convert_f_to_c():
    """Converts input temperature from Fahrenheit to Celsius"""
    try:
        fahrenheit = float(input("Enter Temperature in Fahrenheit:"))
    except ValueError:
        print("Temperature must be a number")
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


def convert_c_to_f():
    """Converts input temperature from Celsius to Fahrenheit"""
    try:
        celsius = float(input("Enter Temperature in Celsius:"))
    except ValueError:
        print("Temperature must be a number")
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")

main()
