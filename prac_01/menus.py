# # algorithm
# get name
# display menu
# get choice
# while choice != Q
#    if choice == H
#        display "hello" name
#    else if choice == G
#        display "goodbye" name
#    else
#        display invalid message
#    display menu
#    get choice
# display finished message
#

# get name
name = input("Enter name:")

# initiate loop
while True:
    print("""(H)ello
(G)oodbye
(Q)uit""")
    # get user response and format to uppercase
    response = input().upper()
    # check responses
    if response == "Q":
        print("Finished!")
        break
    elif response == "H":
        print(f"Hello {name}!")
    elif response == "G":
        print(f"Goodbye {name}!")
    else:
        print("Invalid choice")
