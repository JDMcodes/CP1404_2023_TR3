import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45
def main():
    """Lottery ticket program - chooses random numbers"""
    try:
        number_of_tickets = int(input("How many tickets:"))
    except ValueError:
        print("enter a valid number")
        return
    tickets = ticket_generator(number_of_tickets)
    for i in range(0,len(tickets)):
        tickets[i] = [str(numbers) for numbers in tickets[i]]
        print(" ".join(tickets[i]))


def ticket_generator(number_of_tickets):
    """chooses random numbers for tickets"""
    tickets = []
    for i in range(0, number_of_tickets):
        ticket = []
        for j in range(0, NUMBERS_PER_LINE):
            ticket.append(random.randint(MINIMUM, MAXIMUM))
        ticket.sort()
        tickets.append(ticket)
    return tickets


main()

