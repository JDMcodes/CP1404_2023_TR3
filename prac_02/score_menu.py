"""
score evaluation with menu and functions
"""


def main():
    """Runs functions based on a user input from menu"""
    choice = get_menu_choice()
    #assign score for validation later
    score = -1
    while choice != "Q":
        if choice == "G":
            score = get_score()
            choice = get_menu_choice()
        elif choice == "P":
            if score > 0:
                print(evaluate_score(score))
                choice = get_menu_choice()
            else:
                score = get_score()
                print(evaluate_score(score))
                choice = get_menu_choice()
        elif choice == "S":
            if score > 0:
                print("*" * score)
                choice = get_menu_choice()
            else:
                score = get_score()
                print("*" * score)
                choice = get_menu_choice()

    print("thanks")


def get_menu_choice():
    """Gets user input from menu."""
    menu = """(G)et a valid score
(P)rint result 
(S)how stars 
(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "G" and choice != "P" and choice != "S" and choice != "Q":
        print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    return choice

def get_score():
    score = int(input("Enter score: "))
    while 0 >= score >= 100:
        print("Invalid score, please enter a number from 0 to 100")
    return score

def evaluate_score(score):
    """evaluates a score"""
    if score > 90:
        evaluation = "Excellent"
    elif score >= 50:
        evaluation = "Passable"
    else:
        evaluation = "Bad"
    return evaluation

main()

