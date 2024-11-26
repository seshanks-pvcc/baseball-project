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
        batter = 0
        print(("Top", "Bottom")[inning % 2] + " of the " + convertInning(inning) + " Inning.")
        tick()
        currentPitcher = (home.getCurrentPitcher(), away.getCurrentPitcher())[inning % 2]
        print(currentPitcher.getName() + " pitching for the " + (home.name, away.name)[inning % 2])
        tick()
        while outs >= 3: #loops every at-bat
            currentBatter = (home.batters[batter], away.batters[batter])[inning%2]
            print(currentBatter.getName() + " up to bat!")
            tick()
            batting = True
            while batting: #loops every pitch
                outcome = ""
                pitch = ""
                swing = False
                contact = False
                if random.random() + (0.3 * currentPitcher.perfection) < 0.55: #strike chance should vary from 0.45 to 0.75
                    pitch = "ball"
                else:
                    pitch = "strike"
                if pitch == "strike" and random.random() + (0.2 * currentPitcher.trickiness) < 0.5 + (0.2 * currentBatter.appraisal): #Batters should swing at strikes ~60% of the time, with 10pp variation in both pitcher and batter skill
                    swing = True
                elif pitch == "ball" and random.random() + (0.2 * currentBatter.appraisal) < 0.2 + (0.2 * currentPitcher.trickiness): #Batters should swing at balls ~30% of the time with 10pp variation. Batters not swinging at the ball is good, so the rule is broken in order to have locally consistent code, note the stats are swapped from above
                    swing = True
                if swing:
                    if pitch == "strike" and random.random() + (0.3 * currentPitcher.strength) < 0.7 + (0.3 * currentBatter.twitch): #average 85% success, 15pp var on both
                        contact = True
                    elif pitch == "ball" and random.random() + (0.2 * currentPitcher.strength) < 0.45 + (0.2 * currentBatter.twitch): #average 55% success, 10pp var on both
                        contact = True
                    #swing
                if not contact:
                    if pitch == "ball":
                        balls = balls + 1
                        outcome = "Ball. " + balls + "-" + strikes
                    elif pitch == "strike":
                        strikes = strikes + 1
                        outcome = "Strike, " + (" Looking. ", "Swinging. ")[swing] + balls + "-" + strikes
                else:
                    if random.random() < 0.4 + (0.2 * currentBatter.accuracy): #50% chance of fair ball, 10pp var, pitcher doesn't affect because I don't have it in the doc
                        #TODO implement this
                        hittheball
                    else:
                        if strikes < 2:
                            strikes = strikes + 1
                        outcome = "Foul Ball. " + balls + "-" + strikes
                if strikes >= 3:
                    outcome = currentBatter.getName + " Strikes Out."
                    outs = outs + 1
                    batting = False
                elif balls >= 4:
                    outcome = currentBatter.getName() + " Walks to First Place."
                    # Advancement algorithm. Can't be in function because I need too many results from it. (state of bases, anyone who scored, sometimes I will need to account for runners getting out)
                    if bases[0] == 0:
                        bases[0] = currentBatter
                    elif bases[1] == 0:
                        bases[1] = bases[0]
                        bases[0] = currentBatter
                    elif bases[2] == 0:
                        bases[2] = bases[1]
                        bases[1] = bases[0]
                        bases[0] = currentBatter
                    else:
                        outcome = outcome + " " + bases[2].getName() + " scores 1 Run."
                        bases[2] = bases[1]
                        bases[1] = bases[0]
                        bases[0] = currentBatter
                        if inning % 2:
                            awayRuns = awayRuns + 1
                        else:
                            homeRuns = homeRuns + 1
                

                 

                
        if ((awayRuns == homeRuns) or inning < 18) and not (awayRuns > homeRuns and (inning % 2) == 1 and inning >= 17): #ties and being before the 10th inning cause the game to continue, the away team already winning going into the bottom (the half they score in) of the final inning (9th or extra) causes the game to end regardless.
            bases = [0, 0, 0]
            balls = 0
            strikes = 0
            outs = 0
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



