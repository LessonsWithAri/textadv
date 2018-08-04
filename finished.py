#!/usr/bin/env python3
import random

room_learning_took_soda = False
def room_learning(state):
    global room_learning_took_soda
    print("You are in room #312. You see a Kellan, a Maria, and a Brooke.")
    if not room_learning_took_soda: print("There is a can of soda on the table.")
    print("Exits: DOOR")
    command = input("> ").lower()
    if command == "door":
        print("You have gone through the door.")
        room_hallway(state)
    elif command == "kellan":
        print("Kellan says, 'Hi!'")
        room_learning(state)
    elif command == "maria":
        print("Maria is busy doing coding")
        room_learning(state)
    elif command == "brooke":
        print("Brooke is writing a story")
        room_learning(state)
    elif command == "take the soda" and not room_learning_took_soda:
        print("You pick up the soda. It's nice and cold.")
        room_learning_took_soda = True
        state.inventory.append('soda')
        room_learning(state)
    else:
        print("INVALID COMMAND!!!")
        room_learning(state)

room_hallway_gave_matt_soda = False
def room_hallway(state):
    global room_hallway_gave_matt_soda
    print("You are in the hallway. It's very spoooooky.")
    if not room_hallway_gave_matt_soda: print("Matt is here, he's very thirsty.")
    print("Exits: LEARNING")
    command = input("> ").lower()
    if command == "learning":
        print("You are going back to the learning room.")
        room_learning(state)
    elif command == "give matt the soda" and not room_hallway_gave_matt_soda and 'soda' in state.inventory:
        print("You give Matt the soda. He says thanks, gulps it down, and leaves.")
        state.inventory.remove('soda')
        room_hallway_gave_matt_soda = True
        room_hallway(state)
    else:
        print("INVALID COMMAND!!!")
        room_hallway(state)

class GameState:
    def __init__(self):
        self.inventory = []

state = GameState()

room_learning(state) # this comes last
