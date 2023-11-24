usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    user = input("user:")
    check_username(user)
    numbers = get_numbers()
    print(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average number is {sum(numbers)/len(numbers)}")


def get_numbers():
    numbers = []
    for i in range(0,5):
        try:
            new_number = int(input("Number:"))
            numbers.append(new_number)
        except ValueError:
            print("Number is not an integer")
    return numbers

def check_username(username):
    if username in usernames:
        print("access granted")
    else:
        print("access denied")





main()
