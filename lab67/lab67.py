#!/usr/bin/env python3

count = 0 

with open('dracula.txt') as dracula:
    text = dracula.read()
    for line in text.split('\n'):
        if 'vampire' in line.lower():
            print(line)
            count = count + 1
            with open('vampytimes.txt', 'a') as vampytimes:
                vampytimes.write(line + '\n')
                
print(count)

