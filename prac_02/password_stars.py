"""
Password Check with functions

"""


def main():
    """Prints an input password as a censored copy"""
    password = get_password()
    print_censored_word(password)
    return


def get_password():
    """Validates and stores a password containing no spaces and more than 10 characters"""
    password = input("Please enter new password:")
    if len(password) < 10 or " " in password:
        print("please enter a valid password")
        password = input("Please enter password:")

    return password


def print_censored_word(word):
    """Prints a censored copy of an input word."""
    print("*" * len(word))


main()
