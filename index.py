#!/usr/bin/env python3
name = input("Welcome! What's your name? ")
print(f"Greetings, {name}!")

def room_learning():
    print("You are in room #312. You see a Kellan, a Maria, and a Brooke. Exits are: DOOR")
    command = input("> ").lower()
    if command == "door":
        print("You have gone through the door.")
        room_hallway()
    elif command == "kellan":
        print("Kellan says, 'Hi!'")
        room_learning()
    elif command == "maria":
        print("Maria is busy doing coding")
        room_learning()
    elif command == "brooke":
        print("Brooke is writing a story")
        room_learning()
    else:
        print("INVALID COMMAND!!!")
        room_learning()

def room_hallway():
    print("You are in the hallway. It's very spoooooky. Exits: LEARNING")
    command = input("> ").lower()
    if command == "learning":
        print("You are going back to the learning room.")
        room_learning()
    else:
        print("INVALID COMMAND!!!")
        room_hallway()

room_learning()
