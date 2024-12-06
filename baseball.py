import time
import random
import math

#import class definitions
from Team import *

# Structural variable declarations
program = True

teams = [Team("Testing Testers", "Slogan still under review", "T"), Team("Detroit Bugs", "Punched ya!", "D")] #I am aware this pun is extremely weak, IDR why they are from detroit in the first place.



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

    def output(event):
        words = event.split(" ") #57 characters in the event section of the output
        lines = [""]
        line = 0
        for word in words:
            if len(lines) -1 < line:
                lines.append("")
            if len(lines[line]) + len(word) + 1 <= 57:
                lines[line] = lines[line] + word + " "
            elif len(lines[line]) + len(word) <= 57: #if there is just enough space don't add a trailing space
                lines[line] = lines[line] + word
                line = line + 1
            else:
                lines[line] = lines[line] + (" " * (57 - len(lines[line])))
                line = line + 1
                lines.append(word)
        lines[line] = lines[line] + (" " * (57 - len(lines[line])))
        while len(lines) < 4:
            lines.append(" " * 57)
        for ln in lines:
            if len(ln) < 57:
                print
                ln = ln + (" " * (57 - len(ln)))
            elif len(ln) > 57:
                raise "The output function broke somehow" + "\n" + ln #this shouldn't be reachable but if it happens I want to know about it
        #these get variables because they are variable lengths
        inningBug = ("^","v")[inning%2] + str((inning//2)+1)
        awayScoreBug = str(awayRuns)
        homeScoreBug = str(homeRuns)
        baseOut = []
        for base in bases:
            if base == 0:
                baseOut.append("*")
            else:
                baseOut.append(base.lname[0])
        lines[0] = lines[0] + " " + (" ","")[len(inningBug)>2] + inningBug + (" ","")[len(inningBug)>3] + " " + awayScoreBug + "-" + homeScoreBug
        lines[1] = lines[1] + " " + away.symbol + "@" + home.symbol + "  B:" + ("○","●")[balls>=3] + ("○","●")[balls>=2] + ("○","●")[balls>=1]
        lines[2] = lines[2] + "  " + baseOut[1] + "   S:"  + ("○","●")[strikes>=2] + ("○","●")[strikes>=1]
        lines[3] = lines[3] + " " + baseOut[2] + " " + baseOut[0] + "  O:"   + ("○","●")[outs>=2] + ("○","●")[outs>=1]
        lines.append("-"*70)
        print("\n".join(lines))

    output(str(away.name) + " at " + str(home.name))
    tick()
    while game: #Loops every inning
        pitchingTeam = (home,away)[inning%2]
        battingTeam = (away,home)[inning%2]
        batter = 0
        output(("Top", "Bottom")[inning % 2] + " of the " + convertInning(inning) + " Inning.")
        tick()
        currentPitcher = pitchingTeam.getCurrentPitcher()
        output(currentPitcher.getName() + " pitching for the " + pitchingTeam.name)
        tick()
        while outs <= 3: #loops every plate appearence
            balls = 0
            strikes = 0
            currentBatter = battingTeam.batters[batter]
            output(currentBatter.getName() + " up to bat!")
            tick()
            batting = True
            while batting: #loops every pitch
                outcome = ""
                pitch = ""
                swing = False
                contact = False
                steal = False
                thief = -1
                runsScored = 0
                for runner in range(len(bases)-2, -1, -1):
                    if bases[runner] != 0 and bases[runner+1] == 0 and not steal and random.random() < 0.1 + (0.3 * bases[runner].greed):
                        steal = True
                        thief = runner
                if steal:
                    if random.random() + (0.2 * currentPitcher.vigilence) < 0.5 + (0.2 * bases[thief].sneak):
                        outcome = bases[thief].getName() + " steals " + ("1st", "2nd", "3rd")[thief + 1] + " base!"
                        bases[thief + 1] = bases[thief]
                        bases[thief] = 0
                    else:
                        outcome = bases[thief].getName() + " caught stealing"
                        bases[thief] = 0
                        outs = outs + 1
                    if outs >= 3:
                        batting = False
                else:
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
                            outcome = "Ball. " + str(balls) + "-" + str(strikes)
                        elif pitch == "strike":
                            strikes = strikes + 1
                            outcome = "Strike, " + (" Looking. ", "Swinging. ")[swing] + str(balls) + "-" + str(strikes)
                    else:
                        if random.random() < 0.4 + (0.2 * currentBatter.accuracy): #50% chance of fair ball, 10pp var, pitcher doesn't affect because I don't have it in the doc
                            batting = False
                            distance = random.random() + (currentPitcher.resilience) - (currentBatter.power) #smaller value = more distance
                            defender = random.choice(pitchingTeam.batters)
                            if distance + (0.4 * defender.perception) < 0.4:
                                #If not out: Single rate 65% Double rate 19% Triple rate 1% Home Runs 15% 
                                travelling = distance - currentBatter.speed + defender.chasing # will be used for for far the batter gets
                                hit = 0
                                if travelling > 0.35:
                                    outcome = currentBatter.getName() + " hits a Single."
                                    hit = 1
                                elif travelling > 0.16:
                                    outcome = currentBatter.getName() + " hits a Double."
                                    hit = 2
                                elif travelling > 0.15:
                                    outcome = currentBatter.getName() + " hits a Triple."
                                    hit = 3
                                else:
                                    outcome = currentBatter.getName() + " hits a Home Run!"
                                    hit = 4
                                runsScored = 0
                                for runner in range(len(bases)-1, -1, -1):
                                    if bases[runner] != 0 and hit == 4:
                                        bases[runner] = 0
                                        runsScored = runsScored + 1
                                        if inning % 2:
                                            awayRuns = awayRuns + 1
                                        else:
                                            homeRuns = homeRuns + 1
                                    elif bases[runner] != 0 and random.random() + (0.2 * defender.blocking) < 0.4 + (0.2 * bases[runner].speed):
                                        if len(bases) - runner <= hit:
                                            bases[runner] = 0
                                            runsScored = runsScored + 1
                                            if inning % 2:
                                                awayRuns = awayRuns + 1
                                            else:
                                                homeRuns = homeRuns + 1
                                        elif bases[runner + hit] != 0:
                                            bases[runner + hit] = bases[runner]
                                            bases[runner] = 0
                                    elif bases[runner] != 0:
                                        outcome = outcome + " " + defender.getName() + " tags " + bases[runner].getName() + " out at " + ("1st","2nd","3rd")[runner] + " base."
                                        bases[runner] = 0
                                        outs = outs + 1
                                if hit == 4:
                                    runsScored = runsScored + 1
                                    if inning % 2:
                                        awayRuns = awayRuns + 1
                                    else:
                                        homeRuns = homeRuns + 1
                                else:
                                   bases[hit-1] = currentBatter # it should be impossible for this to overwrite a player and if it does it won't really matter
                            else: #batter gets out on hit
                                batting = False
                                if distance < 0.4:
                                    outcome = "Fly out to " + defender.getName()
                                else:
                                    outcome = "Ground out to " + defender.getName()
                                for runner in range(len(bases)-1, -1, -1):
                                    if bases[runner] != 0:
                                        sacAdv = random.random() + (0.2 * defender.blocking)
                                        if runner == 2:
                                            if sacAdv < 0.2 + (0.2 * bases[runner].plead):
                                                    outcome = outcome + " " + bases[runner].getName() + " scores on the sacrifice."
                                                    runsScored = runsScored + 1
                                                    if inning % 2:
                                                        awayRuns = awayRuns + 1
                                                    else:
                                                        homeRuns = homeRuns + 1
                                                    bases[runner] = 0
                                            elif sacAdv > 0.7 + (0.2 * bases[runner].plead):
                                                outcome = outcome + " " + bases[runner].getName() + " was caught out on the sacrifice."
                                                bases[runner] = 0
                                                outs = outs + 1
                                        else:
                                            if bases[runner + 1] == 0:
                                                if sacAdv < 0.2 + (0.2 * bases[runner].plead):
                                                    outcome = outcome + " " + bases[runner].getName() + " advances on the sacrifice."
                                                    bases[runner + 1] = bases[runner]
                                                    bases[runner] = 0
                                                elif sacAdv > 0.7 + (0.2 * bases[runner].plead):
                                                    outcome = outcome + " " + bases[runner].getName() + " was caught out on the sacrifice."
                                                    bases[runner] = 0
                                                    outs = outs + 1
                                outs = outs + 1
                        else:
                            if strikes < 2:
                                strikes = strikes + 1
                            outcome = "Foul Ball. " + str(balls) + "-" + str(strikes)
                if runsScored:
                    outcome = outcome + " " + str(runsScored) + " Runs Scored."
                output(outcome)
                tick()
                
                if batting and strikes >= 3:
                    output(currentBatter.getName() + " Strikes Out.")
                    outs = outs + 1
                    batting = False
                    tick()
                elif batting and balls >= 4:
                    outcome = currentBatter.getName() + " Walks to First Base."
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
                    output(outcome)
                    tick()
            batter = batter + 1    

                 

                
        if ((awayRuns == homeRuns) or inning < 18) and not (awayRuns > homeRuns and (inning % 2) == 1 and inning >= 17): #ties and being before the 10th inning cause the game to continue, the away team already winning going into the bottom (the half they score in) of the final inning (9th or extra) causes the game to end regardless.
            bases = [0, 0, 0]
            balls = 0
            strikes = 0
            outs = 0
            inning = inning + 1
        else:
            game = False
    print((away.name,home.name)[homeRuns>awayRuns] + " Won " + str((awayRuns,homeRuns)[homeRuns>awayRuns]) + " to " + str((homeRuns,awayRuns)[homeRuns>awayRuns]) + ".")
    if homeRuns > awayRuns:
        home.win()
        away.lose()
    else:
        away.win()
        home.lose()

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



