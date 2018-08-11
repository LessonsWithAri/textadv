#!/usr/bin/env python3
import os
import sys
import random
import pickle

class GameState:
    def __init__(self):
        self.inventory = []
        self.room = 'learning'
        self.rooms = {}
        self.roomstate = {}
    
    def add_room(self, name, func):
        self.rooms[name] = func
        self.roomstate.setdefault(name, {})  # New

    def go_to_room(self, roomname):
        self.room = roomname
        self.save()
        self.rooms[roomname](self, self.roomstate[roomname])

    def save(self):
        with open('textadv.pkl', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def start(self):
        self.go_to_room(self.room)

    def __getstate__(self):
        contents = self.__dict__.copy()
        contents['rooms'] = {}
        return contents


if os.path.isfile('textadv.pkl') and '--clean' not in sys.argv:
    with open('textadv.pkl', 'rb') as f:
        state = pickle.load(f)
        print("Loaded saved game.")
else:
    state = GameState()
    print("Starting new game. Welcome.")


def room_learning(state, roomstate):
    print("You are in room #312. You see a Kellan, a Maria, and a Brooke.")
    if not roomstate.get('took_soda', False): print("There is a can of soda on the table.")
    print("Exits: DOOR")
    command = input("> ").lower()
    if command == "door":
        print("You have gone through the door.")
        state.go_to_room('hallway')
    elif command == "kellan":
        print("Kellan says, 'Hi!'")
        state.go_to_room('learning')
    elif command == "maria":
        print("Maria is busy doing coding")
        state.go_to_room('learning')
    elif command == "brooke":
        print("Brooke is writing a story")
        state.go_to_room('learning')
    elif command == "take the soda" and not roomstate.get('took_soda', False):
        print("You pick up the soda. It's nice and cold.")
        roomstate['took_soda'] = True
        state.inventory.append('soda')
        state.go_to_room('learning')
    else:
        print("INVALID COMMAND!!!")
        state.go_to_room('learning')

state.add_room('learning', room_learning)

def room_hallway(state, roomstate):
    print("You are in the hallway. It's very spoooooky.")
    if not roomstate.get('gave_soda', False): print("Matt is here, he's very thirsty.")
    print("Exits: LEARNING")
    command = input("> ").lower()
    if command == "learning":
        print("You are going back to the learning room.")
        state.go_to_room('learning')
    elif command == "give matt the soda" and not roomstate.get('gave_soda', False) and 'soda' in state.inventory:
        print("You give Matt the soda. He says thanks, gulps it down, and leaves.")
        state.inventory.remove('soda')
        roomstate['gave_soda'] = True
        state.go_to_room('hallway')
    else:
        print("INVALID COMMAND!!!")
        state.go_to_room('hallway')

state.add_room('hallway', room_hallway)

state.start()
