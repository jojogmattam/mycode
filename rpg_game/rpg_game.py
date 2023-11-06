#!/usr/bin/python3

import os
from layout import *
import riddle

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')  
        
def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      teleport to [room]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the number of moves
    print('---------------------------')
    print('Moves: ' + str(moves_counter))
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    show_directions()
    available_directions = ', '.join(currentRoom_directions)
    print('You can go only in the directions - ' + available_directions)
    # empty the currentRoom_directions list
    currentRoom_directions.clear()
    # print what the player is carrying
    print('Inventory: ', inventory)
    if teleport_counter > 0:
      print(f'Teleport left: ' + str(teleport_counter))
    print()
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      item_keys = list(rooms[currentRoom]['item'].keys())
      print('You see a ' + ', '.join(item_keys))
    print("---------------------------")

# directions you can go from a room
def show_directions():
    if rooms[currentRoom]:
        for direction in directions:
            if direction in rooms[currentRoom]:
                currentRoom_directions.append(direction)


# start the player in the Hall
currentRoom = 'Hall'

# an inventory, which is initially empty
inventory = []

# a list of directions for current room which is initially empty
currentRoom_directions = []

# start the move count with zero
moves_counter = 0

# start the teleport counter with zero
teleport_counter = 0

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #clear terminal
        clear()
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom] and 'key' in inventory:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            #add one to move counter
            moves_counter += 1
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #clear terminal
        clear()
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #description of the item
            print()
            print('Description of the item:')
            print(rooms[currentRoom]['item'][move[1]])
            print()
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'teleport':
        clear()
        if teleport_counter > 0 and move[1].capitalize() in rooms:
            currentRoom = move[1].capitalize()
            teleport_counter -= 1
            moves_counter += 1
            print('Teleporting to ' + move[1])
        elif teleport_counter == 0:
            print('You have no teleports left')
            print()
        else:
            print("We can't find that room in the map")
            print()   

    #if inventory has crystal add the teleport counter to 1
    if 'crystal' in inventory:
        teleport_counter += 2
        print()
        print('Crystal vanished into thin air and gave you 2 teleports power')
        print()
        del inventory[inventory.index('crystal')]


    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    # Define alternate way to defeat monster by playing a game
    if currentRoom == 'Garden' and 'key' in inventory:
        print('You dont have the potion to kill the monster, You can play a simple game to defeat the monster if you are smart')
        choice = input('Do you want to play a game? (y/n)')
        if choice == 'y':
            riddle.initial_instructions()
            print("You escaped the house with the key and your intelligence, YOU WIN!")
        else:
            print('You can\'t defeat the monster without the potion, monster got you, GAME OVER!')
            break

if __name__ == '__main__':
    showInstructions()
    showStatus()

