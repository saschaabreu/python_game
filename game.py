import time
import random


def dprint(delay, text):
    """ Print, then delay """
    print(text)
    time.sleep(delay)


def playLabyrinth():
    """ Play the labyrinth with ten choices """

    dprint(2, "You entered a hallway.")

    # chose randomly how many games to play
    numberOfGames = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # repeat the same question
    for i in range(numberOfGames):

        # randomly determine the correct direction
        correct = random.choice(["Left", "Right"])

        # choose direction
        while True:
            chosen = input("\nDo you want to go left or right?\
                \n'Left', 'Right'\n")

            if chosen == correct:
                # this moves player forward
                dprint(2, "You walk down the hallway.")
                dprint(1, "...")
                dprint(2, "There is an intersection ahead.")
                break

            else:
                # this makes player go back and choose again
                # (must change choice from before)
                dprint(3, "Seems like this way is a dead end. You go back.")

    dprint(3, "At the end of this hallway is a door.")
    dprint(2, "You walk to the door..")

    # make player open the door
    while True:
        action = input("\nDo you want to open the door?\n'Yes', 'No'\n")
        print()
        if action == "No":
            # make player choose again, must open door
            dprint(3, "There is nothing else to do here.")
        elif action == "Yes":
            # this leads the player to the final room
            dprint(5, "You slowly open the door")
            dprint(1, "... click!")
            dprint(5, "It unlocked!")
            break

    # play the final room now
    playFinalRoom()


def playFinalRoom():
    """ Play the final room (last room in the game) """
    dprint(3, "You enter the room.")
    dprint(4, "A cold breeze blows.")
    dprint(3, "You see a window to the outside!")
    dprint(3, "There is a door right next to the window.")

    # choose if going through door
    # (not really a choice)
    while True:
        action = input("\nDo you want to go through the door?\n'Yes', 'No'\n")
        print()
        if action == "Yes":
            # go through door and win!
            dprint(2, "You approach the door")
            dprint(5, "You try to turn the door knob")
            dprint(2, "It opens!")
            dprint(3, "You are finally outside!")
            dprint(5, "Congratulations!")
            break
        elif action == "No":
            # ask player to choose again..
            dprint(2, "You look around the room")
            dprint(4, "There is nothing interesting around")


def playGame():
    """ Play one game """
    dprint(1, "Welcome to the game!\n")

    dprint(1, "...")
    dprint(2, "You hear the sound of a door closing.")
    dprint(3, "You open your eyes, waking up from a nap.")
    dprint(4, "You don't know how long you were asleep and you don't know \
        where you are.")

    # choose an action
    while True:
        action = input("\nWhat do you want to do?\n'Get up', 'Go back to \
            sleep'\n")
        print()
        if action == "Get up":
            # this continues the game
            break
        elif action == "Go back to sleep":
            # this ends the game
            print()
            return

    dprint(3, "You get up and look around the room")
    dprint(4, "There are no windows and two doors, one on your left, one on \
        your right.")

    # choose a door
    while True:
        action = input("\nWhich door do you choose?\n'Left', 'Right'\n")
        print()
        if action == "Left":
            # this continues the game
            break
        elif action == "Right":
            # this also continues the game
            break

    # the player just chose a door
    # choose next room at random
    # either final room (almost done)
    # or labyrinth (many choices)

    # randomly choose if player goes directly to final room or labyrinth!
    if random.random() > 0.5:
        playFinalRoom()
    else:
        playLabyrinth()

    dprint(4, "You finished the game!")
    print()


while True:
    # play one game
    playGame()

    # ask if player wants to play another game
    again = input("Would you like to play again?\n(enter 'Yes' for another \
        game, anything else to quit)\n")
    print()

    if again == "Yes":
        # if yes, do no nothing and the 'while' loop will go again
        dprint(2, "Starting another game, please wait...\n")
        dprint(1, "----------------- new game --------------------\n")
    else:
        # if no, quit the loop, then the program will stop
        dprint(1, "Good bye!")
        break
