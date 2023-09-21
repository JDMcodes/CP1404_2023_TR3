def main():
    password = get_password()
    print_censored_password(password)
    return


def get_password():
    while True:

        password = input("Please enter password:")

        if len(password) < 10:
            print("please enter a password with more than 10 characters")
            continue
        if " " in password:
            print("password cannot contain spaces")
            continue
        break

    return password


def print_censored_password(password):
    for i in range(1, len(password)):
        print("*")


main()
