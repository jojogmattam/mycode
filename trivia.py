#!/usr/bin/env python3

import requests
import random
import os
import html

categories= {
9:  "General Knowledge", 
10: "Entertainment- Books", 
11: "Entertainment- Film", 
12: "Entertainment- Music", 
13: "Entertainment- Musicals & Theater", 
14: "Entertainment- Television", 
15: "Entertainment- Video Games", 
16: "Entertainment- Board Games", 
17: "Science- Nature", 
18: "Science- Computers", 
19: "Science- Mathematics", 
20: "Mythology", 
21: "Sports", 
22: "Geography", 
23: "History", 
24: "Politics", 
25: "Art", 
26: "Celebrities", 
27: "Animals", 
28: "Vehicles", 
29: "Entertainment- Comics", 
30: "Science- Gadgets", 
31: "Entertainment- - Japanese Anime & Manga", 
32: "Entertainment- - Cartoon Animations"
}

base_url = "https://opentdb.com/api.php"

score = 0
count = 0
answers = []

def main():
    params = ask_params()
    url = build_url(base_url, params)
    game(url)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ask_params():
    global count
    clear()
    print("***TRIVIA***\n")
    no_qsts = int(input("How many questions would you like to answer? "))
    count = no_qsts
    #show categosries and ask user to choose
    clear()
    print(f"\n***CHOOSE CATEGORY***\n")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {categories[category]}")
        #ask user to choose 
    category = int(input("What category would you like to answer? "))
    # assiging key value of catergories to variable
    category = list(categories.keys())[category-1]
    #ask user to choose difficulty
    clear()
    print(f"\n***DIFFICULTY LEVEL***\n")
    print(f"1.Easy\n2.Medium\n3.Hard")
    difficulty = int(input("What difficulty would you like to answer? "))
    if difficulty == 1:
        difficulty = "easy"
    elif difficulty == 2:
        difficulty = "medium"
    elif difficulty == 3:
        difficulty = "hard"
    else:
        print("Invalid input")
    #ask user to choose type
    clear()
    print(f"\n***TYPE OF QUESTION**\n")
    print(f"1.Multiple\n2.Boolean")
    type = int(input("What type of question would you like to answer? "))
    if type == 1:
        type = "multiple"
    elif type == 2:
        type = "boolean"
    else:
        print("Invalid input")

    params = {
        "amount": no_qsts,
        "category": category,
        "difficulty": difficulty,
        "type": type
    }
    # print params
    clear()
    print("\n***PARAMS YOU CHOSE***\n")
    for key, value in params.items():
        print(f"{key}: {value}")
    return params

def build_url(base_url, params):
    url = requests.get(base_url, params=params)
    return url.url

def game(url):
    global score
    data= requests.get(url).json()
    i = 1
    #Ask questions
    for question in data["results"]:
        print(f"\n--Question:{i}--\n")
        i += 1
        question["question"] = html.unescape(question["question"])
        print(question["question"])
        #Add correct answer to list and randomize list and show to user      
        answers.append(html.unescape(question["correct_answer"]))
        answers.extend(html.unescape(question["incorrect_answers"]))
        random.shuffle(answers)
        # show user the answers with nummbers
        for index, answer in enumerate(answers, start=1):
            print(f"{index}. {answer}")
        #ask user for answer
        answer = int(input("Enter your answer: "))
        # check if answer is correct
        if answers[answer-1] == question["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        
        answers.clear()
        
    print(f"\n***GAME STATS***")    
    print(f"You answered {score}/{count} questions correctly.\n")
    play_again()

def play_again():
    global score
    global count
    again = input("Would you like to play again? (y/n) ")
    if again == "y":
        score = 0
        count = 0
        main()
    else:
        print("Thanks for playing!")
        exit()

if __name__ == "__main__":
    main()
