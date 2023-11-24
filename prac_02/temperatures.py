"""

Temperature converter with functions.
"""


def main():
    """Converts temperature based on a user selection from a menu"""
    temperature_unit = get_temperature_unit()
    if temperature_unit == "F":
        fahrenheit = convert_f_to_c()
        print(f"Result: {fahrenheit:.2f} F")
    elif temperature_unit == "C":
        celsius = convert_c_to_f()
        print(f"Result: {celsius:.2f} C")
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
    fahrenheit = float(input("Enter Temperature in Fahrenheit:"))
    return 5 / 9 * (fahrenheit - 32)



def convert_c_to_f():
    """Converts input temperature from Celsius to Fahrenheit"""
    celsius = float(input("Enter Temperature in Celsius:"))
    return celsius * 9.0 / 5 + 32

main()
