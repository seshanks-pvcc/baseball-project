import time
import random
import math

# Structural variable declarations
program = True
game = False
teams = ["Testing Testers", "Detroit Bugs"]
bases = [0, 0, 0]
balls = 0
strikes = 0
outs = 0
inning = 1


# Function modules

# tms is a length 2 list of the teams playing against each other, the latter being the home team
def runGame(tms):
    print(str(tms[0]) + " at " + str(tms[1]))

def openTeam(team):
    print(team)

def openGame():
    print("This hasn't been finished yet")
    playingTeams = []
    while(len(playingTeams) < 2):
        # zip creates a list of tuples in the form ("n)", nth team) and this list comprehension makes that into a list of strings in the form "n) nth team", which is then joined by newlines
        menu = "\n".join(["".join(pair) for pair in zip(map(lambda x: str(x+1) + ") ", range(len(teams))), teams)] + ["99) End"])
        print(menu)
        option = input()
        if(int(option)-1 in range(len(teams)) and option != "99" and teams[int(option)] not in playingTeams):
            playingTeams.append(teams[int(option)-1])
            print(playingTeams)
        elif (option != "99" and teams[int(option)-1] in playingTeams):
            print("You have already selected that team")
        elif (option == "99"):
            return
        else:
            print("Please select a valid option")
    runGame(playingTeams)

def listTeams():
    print("This hasn't been finished yet")
    menu = "\n".join(["".join(pair) for pair in zip(map(lambda x: str(x+1) + ") ", range(len(teams))), teams)] + ["99) End"])
    print(menu)
    option = input()
    if(int(option)-1 in range(len(teams)) and option != "99"):
        openTeam(teams[int(option)-1])
    elif (option == "99"):
        return
    else:
        print("Please select a valid option")
        listTeams()


print("Welcome to Emily's baseball simulation \n")
#Main loop
while(program):
    print("Select an option:\n" + "1) Run Game\n" + "2) List Teams\n" + "99) End")
    option = input()
    match option:
        case "1":
            openGame()
        case "2":
            listTeams()
        case "99":
            print("Thanks for playing")
            program = False
        case _:
            print("Please select a valid option:")



