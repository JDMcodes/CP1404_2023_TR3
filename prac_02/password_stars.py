def main():
    password = get_password()
    print_censored_password(password)
    return


def get_password():
    password = input("Please enter password:")
    if len(password) < 10 or " " in password:
        print("please enter a valid password")

    return password


def print_censored_password(password):
    for i in range(1, len(password)):
        print("*")


main()
