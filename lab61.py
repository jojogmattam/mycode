#!/usr/bin/env python3

num = int(input("How many bottles of beer are on the wall? "))

if num > 100:
    print("You can't count down from more than 100 bottles!")
    exit()

for i in range(num, 0, -1):
    print(i, "bottles of beer on the wall!", i, "bottles of beer! You take one down, pass it around!")
    print()
    print(i-1, "bottles of beer on the wall!")


