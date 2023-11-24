"""
CP1404/CP5632 Practical 5
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania"}

MAX_KEY_LEN = len(max(CODE_TO_NAME, key=len))
MIN_KEY_LEN = len(min(CODE_TO_NAME, key=len))
MAX_VALUE_LEN = len(CODE_TO_NAME[max(CODE_TO_NAME, key=len)])
MIN_VALUE_LEN = len(CODE_TO_NAME[min(CODE_TO_NAME, key=len)])



def main():
    """Turn short state codes to full names, then prints the entire key"""
    decode_short_state()
    print_state(CODE_TO_NAME)


def decode_short_state():
    """Turn short state codes to full names"""
    while True:
        try:

            state_code = input("Enter short state: ").upper()
            if state_code == "":
                break
            print(state_code, "is", CODE_TO_NAME[state_code])
            break
        except KeyError:
            print("Invalid short state")


def print_state(state_codes):
    """Print short state key for changing to full name"""
    for state in state_codes:
        print(f"{state:<{MAX_KEY_LEN}} is {state_codes[state]:<{MAX_VALUE_LEN}}")

main()


