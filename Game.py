import time
from Team import *
import random

# This is a possible refactor that would allow multiple games to run at the same time.
# instead of having a loop that controls the game, each Game object would keep its own state and have a sort of "instruction pointer" that would keep track of what piece of code would need to be run next tick.
# This would enable the system to instruct each running game to do its next step and return the output message, then combine them to fit the terminal
# however this would involve translating the existing logic into something that is more similar to BASIC or other goto heavy languages, so it would make writing a design document harder (as the pseudo code and real code will be very different) and thus I will not be implementing it at this moment

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
class Game:

    def __init__(self, home, away): #both are Team objects.
        self.home = home
        self.away = away

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
            print((home.getCurrentPitcher().getName(), away.getCurrentPitcher().getName())[inning % 2] + " pitching for the " + (home.name, away.name)[inning % 2])
            tick()
            if (awayRuns == homeRuns) or inning < 18:
                inning = inning + 1
            else:
                game = False