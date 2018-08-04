#!/usr/bin/env python3

INVENTORY = []
name = input("What's your name? ");

##
# 1. Convert data into serializable format
# 2. Store data when we change it
# 3. Read state when we start
## 

print("Hello, " + name + "!");

def room_office(state):
    print("You are in an office. In front of you is a desk with a computer and a can of soda. To your left is a wall with a whiteboard on it. To your right are floor-to-ceiling windows. Behind you is a door.")
    
    command = input("$ ")
    
    if command == "door":
        room_hallway();
    elif command == "soda":
        print("You pick up the soda. It's very cold.")
        INVENTORY.append('soda')
        room_office()
    else:
        print("INVALID COMMAND!")
        room_office()

room_hallway_gave_soda = False
def room_hallway():
    global room_hallway_gave_soda
    print("You are now in the hallway.")
    if not room_hallway_gave_soda:
        print("Matt is here.")
    print("You can go down the hallway or go back into the room.")
    command = input("$ ")
    if command == 'give matt the soda' and 'soda' in INVENTORY and not room_hallway_gave_soda:
        print("You give matt the soda. He gulps it down thankfully, and leaves.")
        room_hallway_gave_soda = True
        INVENTORY.remove('soda')
        room_hallway()
    else:
        print("INVALID COMMAND!")
        room_hallway()

    
class GameState:
    def __init__(self):
        self.inventory = []

state = GameState()

room_office(state) # this must be last
