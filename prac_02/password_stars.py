def main():
    """Prints an input password as a censored copy"""
    password = get_password()
    print_censored_word(password)
    return


def get_password():
    """Validates and stores a password containing no spaces and more than 10 characters"""
    new_password = input("Please enter new password:")
    if len(new_password) < 10 or " " in new_password:
        print("please enter a valid password")
        new_password = input("Please enter password:")

    return new_password


def print_censored_word(word):
    """Prints a censored copy of an input word."""
    print("*" * len(word))


main()
