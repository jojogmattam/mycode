#!/usr/bin/env python3
import random

question_bank = {
    "What is the command to print something in python?": "print()",
    "What is the command to create a empty file in linux?": "touch",
    "What is the command to delete a file in linux?": "rm",
    "What is the command to create a folder in linux?": "mkdir",
    "What is the command to delete a folder in linux?": "rmdir",
    "What is the command to copy a file in linux?": "cp",
    "What is the command to move a file in linux?": "mv",
    "What is the command to view the current working directory in linux?": "pwd",
    "What is the command to view the files in linux?": "ls",
    "What is the command to view running processes in linux?": "ps",
    "What is the command to view the system information in linux?": "uname"
    }

no_of_qstns = len(question_bank)

def main():
    print("***************Welcome to the Quiz Game!***********************")
    while True:
        try:
            num = int(input(f"\nWe have {no_of_qstns} questions available in the question bank.\nHow many questions do you want to answer?: "))
            if 1 <= num <= no_of_qstns:
                break
            else:
                print(f"\nPlease enter a number between 1 and {no_of_qstns}")
        except ValueError:
            print("\nPlease enter a valid number.")
            
    game(num)


def play_again():
    again = input("Do you want to play again? (y/n): ")
    if again.lower() == "y":
        main()
    else:
        print("Thank you for playing!")
        exit()


def game(num):        
    counter = 0
    score = 0
    question_list = list(question_bank.keys())

    while counter < num:
        question = random.choice(question_list)
        question_list.remove(question)
        answer = input(f"{question}\n")
        if answer.lower() == question_bank[question].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is {question_bank[question]}")
            
        counter += 1

    print(f"You got {score} out of {num} correct.")
    play_again()
    
if __name__ == "__main__":
    main()
