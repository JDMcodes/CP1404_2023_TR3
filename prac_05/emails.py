"""
CP1404/CP5632 Practical 5
Emails to names
Estimate: 20 minutes
Actual:   15 minutes
"""

def main():
    """Compile a dictionary of names and emails"""
    emails_names = {}
    email = input("Enter your email: ")
    while email != "":
        name = find_name_with_email(email)
        confirmation = input(f"Is your name {name}? (y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Enter your name: ")
        emails_names[email] = name
        email = input("Enter your email: ")

    for email, name in emails_names.items():
        print(f"{name} ({email})")


def find_name_with_email(email):
    """Finds name from email"""
    email_name = email.split('@')[0]
    parts = email_name.split('.')
    name = " ".join(parts).title()
    return name


main()