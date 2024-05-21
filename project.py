"""
This program will randomly set an arthmetic question for the user and expect an answer from the user in the nearest round number.
If the user gets wrong answer, the program will display the correct answer and ask if you want to answer next question.
If user gets the answer correct, the program with compliment and ask if you want to answer next question.
Apart from this the program will keep track of the score and will save the score along with the questions that were asked along with the answers to the file.
P.S: This program is a game where all the details of the user is taken first and saved along with the score file.
"""

import cowsay
from random import randint
import os, sys


def main():
    try:
        player = input("What's your name? ").title()
        if "," in player:
            _ , first = player.strip().split(", ")
            message = f"WELCOME, {first}".strip()
        else:
            message = f"WELCOME, {player}".strip()

        cowsay.tux(message)

        user_score = get_user_score(player)  # Will return either False or Score
        if user_score == False:
            update_user_points(False, player, 0)
            user_score = 0
        print(f"\nYour Current Score {user_score}")

        user_choice = '1'
        while user_choice == '1':
            question, result = math_question()
            if -50000 < result < 50000:
                score = user_interaction(question, result, user_score)
                update_user_points(False, player, score)
                user_score = get_user_score(player)
                user_choice = input(f"\nYour Score {user_score} \n \n \t1 - Next question\n \t2 - Exit \n").lower()
            else:
                pass
    except Exception as e:
        sys.exit("An error occured, program exited")


def get_user_score(player):
    if not os.path.exists("/workspaces/55106416/Project/user_score.txt"):
        f = open("/workspaces/55106416/Project/user_score.txt", "w")

    else:
        f = open("/workspaces/55106416/Project/user_score.txt", "r")

    lines = f.readlines()
    f.close()
    content = {}
    for line in lines:
        a = line.strip().split(" - ")
        content.update({a[0]: a[1]})

    for i in content:
        if i == player:
            return content[i]
    return False


def update_user_points(new_user: bool, user_name: str, score: int):
    if new_user:
        with open("/workspaces/55106416/Project/user_score.txt", "a") as file:
            file.write(f"{new_user} - {score}")

        return "Points Updated for New User"
    else:
        with open("/workspaces/55106416/Project/user_score.txt") as file1:
            read_file = file1.readlines()

        content = {}
        for line in read_file:
            a = line.strip().split(" - ")
            content.update({a[0]: a[1]})

        content.update({f"{user_name}": f"{score}"})
        with open("/workspaces/55106416/Project/user_score.txt", "w") as file2:
            for key, value in content.items():
                file2.write(f"{key} - {value}\n")

        return "Points Updated for Existing User"


def math_question():
    operand_list = []
    operator_list = []
    operator_dict = {1: "+", 2: "-", 3: "*", 4: "/", 5: "**"}
    question_string = ""

    for _ in range(5):
        operand_list.append(randint(1, 9))

    for i in range(4):
        operator_list.append(operator_dict[randint(1, 5)])
        if operator_list[i] == operator_list[i - 1]:
            if operator_list[i] == "**":
                operator_list.pop(i)
                operator_list.insert(i, operator_dict[randint(1, 4)])

    for j in range(5):
        if j == 4:
            question_string = question_string + str(operand_list[j])
        else:
            question_string = (
                question_string + str(operand_list[j]) + str(operator_list[j])
            )

    try:
        result = eval(question_string)
        result = round(result)
    except ZeroDivisionError:
        return math_question()

    question_user = question_string.replace("**", "^")

    return question_user, result


def user_interaction(question: str, answer: int, score: int):
    try:
        print("Question:", question)
        user_answer = int(input("Answer: "))
        if user_answer == answer:
            user_score = int(score) + 1
            print("\nWell Done !")
            return str(user_score)
        else:
            print(f"\nCorrect Answer: {answer}\nBetter luck next time :)")
            return score
    except ValueError:
        print("\nEnter numeric value for the answer")


if __name__ == "__main__":
    main()
