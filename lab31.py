#!/usr/bin/env python3

import random

def main():
    wordbank = ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    wordbank.append(4)
    print(wordbank)

    num = int(input(f"Choose a number between 0 and {len(tlgstudents)}: "))
    student_name = tlgstudents[num]

    print(f"{student_name} always use {wordbank[2]} {wordbank[1]} to indent.")

    random_name = random.choice(tlgstudents)
    print(f"Random name from list is {random_name}")

if __name__ == "__main__":
    main()
