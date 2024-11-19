import time
import random
import math

#import class definitions
from Team import *

# Structural variable declarations
program = True

teams = [Team("Testing Testers", "Slogan still under review"), Team("Detroit Bugs", "Punched ya!")] #I am aware this pun is extremely weak, IDR why they are from detroit in the first place.



# Function modules
def tick():
    time.sleep(0.2)

def convertInning(num):
    inning = (num // 2) + 1
    if((inning // 10) % 10 == 1):
        return str(inning) + "th"
    elif (inning % 10 == 1):
        return str(inning) + "st"
    elif (inning % 10 == 2):
        return str(inning) + "nd"
    elif (inning % 10 == 3):
        return str(inning) + "rd"
    else:
        return str(inning) + "th"

# tms is a length 2 list of the teams playing against each other, the latter being the home team
def runGame(tms):
    game = True
    bases = [0, 0, 0]
    balls = 0
    strikes = 0
    outs = 0
    inning = 0
    away = tms[0]
    awayRuns = 0
    home = tms[1]
    homeRuns = 0
    print(str(away.name) + " at " + str(home.name))
    tick()
    while game: #Loops every inning
        print(("Top", "Bottom")[inning % 2] + " of the " + convertInning(inning) + " Inning.")
        tick()
        print((home.getCurrentPitcher().getName(), (away.getCurrentPitcher().getName())[inning % 2] + " pitching for the " + (home.name, away.name)[inning % 2])
        tick()
        if (awayRuns == homeRuns) or inning < 18:
            inning = inning + 1
        else:
            game = False

def openTeam(team):
    opening = True
    while opening:
        team.displayDetail(True)
        print("99) End\nSelect a player for more details")
        option = input()
        if option != "99":
            try:
                team.getPlayer(int(option)).displayDetail()
            except: 
                print("Invalid input")
            input()
        else:
            opening = False
        

def openGame():
    print("This hasn't been finished yet")
    playingTeams = []
    while(len(playingTeams) < 2):
        # zip creates a list of tuples in the form ("n)", nth team) and this list comprehension makes that into a list of strings in the form "n) nth team", which is then joined by newlines
        menu = "\n".join(["".join(pair) for pair in zip(map(lambda x: str(x+1) + ") ", range(len(teams))), map(str, teams))] + ["99) End"])
        print(menu)
        option = input()
        if(option.isdigit() and int(option)-1 in range(len(teams)) and option != "99" and teams[int(option) - 1] not in playingTeams):
            playingTeams.append(teams[int(option)-1])
            print(" ".join([tm.name for tm in playingTeams])) # this is debug
        elif (option != "99" and teams[int(option)-1] in playingTeams):
            print("You have already selected that team")
        elif (option == "99"):
            return
        else:
            print("Please select a valid option")
    runGame(playingTeams)

def listTeams():
    print("This hasn't been finished yet")
    menu = "\n".join(["".join(pair) for pair in zip(map(lambda x: str(x+1) + ") ", range(len(teams))), map(str, teams))] + ["99) End"])
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



