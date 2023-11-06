import random
import time
import os

ascii_art_files = {
    1: 'one.txt',
    2: 'two.txt',
    3: 'three.txt',
    4: 'four.txt',
    5: 'five.txt',
    }


secret_answer= 5
initial_sequence = [1, 2]

#define function to clear the screen based on os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')  

# game will display a random ascii art file and the answer will be the previous one, keep on looping 10 times
def start_game():
    global secret_answer
    question_list = ["Then, what is this?", "But, what is this?", "But, this?", "And, this?", "How about this?"]
    # make the initial sequence
    for i in range(2):
        clear()
        # display the ascii art file
        with open(ascii_art_files[initial_sequence[i]], "r") as f:
            print(f.read())
        time.sleep(1)

        question = random.choice(question_list)
        answer = int(input(question + "\n"))
        if answer == secret_answer:
            print("Correct")
            secret_answer = initial_sequence[i] 
            time.sleep(1)
        else:
            print("Incorrect! Monster got you, Game over")
            exit()

    for i in range(10):
        clear()
        # generate a random number between 1 and 5
        random_number = random.randint(1, 5)
        while random_number == secret_answer:
            random_number = random.randint(1, 5)
        
        # display the ascii art file
        with open(ascii_art_files[random_number], "r") as f:
            print(f.read())

        question = random.choice(question_list)
        answer = int(input(question + "\n"))
        if answer == secret_answer:
            print("Correct")
            secret_answer = random_number
            time.sleep(1)
        else:
            print("Incorrect! Monster got you, Game over")
            exit()

def initial_instructions():   
    # display the file one.txt on screen
    with open('one.txt', "r") as f:
        print(f.read())

    # Wait for Enter key press
    input("Press Enter to start the game")

    # display the file two.txt on screen
    clear()
    with open('two.txt', "r") as f:
        print(f.read())

    print("If this is 1")
    # sleep for 1 second
    time.sleep(2)

    #display the file three.txt on screen

    clear()

    with open('three.txt', "r") as f:
        print(f.read())

    print("If this is 2")
    time.sleep(2)

    # display the file four.txt on screen

    clear()

    with open('four.txt', "r") as f:
        print(f.read())
        
    print("If this is 3")

    time.sleep(2)

    # display the file five.txt on screen

    clear()

    with open('five.txt', "r") as f:
        print(f.read())
        
    print("If this is 4")

    time.sleep(2)
    start_game()


if __name__ == "__main__":
    initial_instructions()







