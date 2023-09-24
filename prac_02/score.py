"""

Program to determine score status
"""
import random


def main():
    """Gets a user score and passes an evaluation, repeats this process on a random score"""
    score = float(input("Enter score: "))
    while 0 >= score >= 100:
        print("Invalid score, please enter a number from 0 to 100")
    evaluation = evaluate_score(score)
    print("score is " + evaluation)
    random_score = random.randint(0, 100)
    random_evaluation = evaluate_score(random_score)
    print("random score is " + random_evaluation)


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