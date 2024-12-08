#Team.py
import random 

#Converts a value from 0 to 1 to a str of stars from 0 stars to 5 stars 
def toStars(stat):
    return ("☆","★")[stat >= 0.2] + ("☆","★")[stat >= 0.4] + ("☆","★")[stat >= 0.6] + ("☆","★")[stat >= 0.8] + ("☆","★")[stat >= 1]

def genfname(inp):
    #Will pick a name from a list, or will generate a name from a set of alternating "consonants" and "vowels"
    #debug names below
    #return ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th")[inp]
    namelist = open("firstnames.csv", "r")
    name = random.choice(namelist.read().split("\n"))
    namelist.close()
    return name

def genlname(inp):
    namelist = open("lastnames.csv", "r")
    name = random.choice(namelist.read().split("\n"))
    namelist.close()
    return name

#for fun, a function that is never run in normal use but generates and prints an arbitrary amount of baseball names
def genNames(num):
    for i in range(num):
        print(genfname(0) + " " + genlname(0))


class Player:
    #defined here so that it can be referred to by all players
    positions = ("Catcher","First Base","Second Base","Third Base","Shortstop","Left Field","Right Field","Center Field", "Pitcher")
    
    def __init__(self, fname = "Wyatt", lname = "Mason", position = 0):
        self.fname = fname #first name
        self.lname = lname #last name
        self.position = position #refers to an element of positions
        
        #batting stats
        self.power       = random.random()     #(affects the amount of bases that can be run off of a hit (by affecting how far the ball goes))
        self.appraisal   = random.random()     #(affects swinging at balls/strikes)
        self.accuracy    = random.random()     #(affects foul/fair balls)
        self.twitch      = random.random()     #(affects the chance of hitting on swing)

        #pitching stats
        self.strength    = random.random()     #(counters twitch)
        self.trickiness  = random.random()     #(counters appraisal)
        self.resilience  = random.random()     #(counters power)
        self.perfection  = random.random()     #(affects strike chance)

        #baserunning stats
        self.speed       = random.random()     #(affects the ability of players to run without being caught)
        self.greed       = random.random()     #(affects how often the player attempts to steal)
        self.sneak       = random.random()     #(counters vigilence)
        self.plead       = random.random()     #(affects advance on outs)

        #defense stats
        self.vigilence   = random.random()     #(catching base stealers)
        self.perception  = random.random()     #(catching hits)
        self.blocking    = random.random()     #(prevents runners from advancing)
        self.chasing     = random.random()     #(counters speed)
        
    def getPosition(self):
        return self.positions[self.position]
        
    def averageBatting(self):
        return (self.power + self.appraisal + self.accuracy + self.twitch) / 4
        
    def averagePitching(self):
        return (self.strength + self.trickiness + self.resilience + self.perfection) / 4
        
    def averageBaserunning(self):
        return (self.speed + self.greed + self.sneak + self.plead) / 4
        
    def averageDefense(self):
        return (self.vigilence + self.perception + self.blocking + self.chasing) / 4
        
    def __str__(self):
        # 48 is the longest possible combination of names.
        return self.fname + " " + self.lname + ", " + (" " * (48 - (1 + len(self.fname) + len(self.lname)))) + self.getPosition() + ": " + (" " * (12 - len(self.getPosition()))) + toStars((self.averageBatting(), self.averagePitching())[self.getPosition() == self.positions[-1]])
    
    def getName(self, full=True):
        if full:
            return self.fname + " " + self.lname
        else:
            return self.lname
    
    def displayDetail(self):
        print(self.fname + " " + self.lname + ", " + self.getPosition())
        print("Batting:      " + str(self.averageBatting()))
        print("  Power:      " + str(self.power))
        print("  Appraisal:  " + str(self.appraisal))
        print("  Accuracy:   " + str(self.accuracy))
        print("  Twitch:     " + str(self.twitch))
        print("Pitching:     " + str(self.averagePitching()))
        print("  Strength:   " + str(self.strength))
        print("  Trickiness: " + str(self.trickiness))
        print("  Resilience: " + str(self.resilience))
        print("  Perfection: " + str(self.perfection))
        print("Baserunning   " + str(self.averageBaserunning()))
        print("  Speed:      " + str(self.speed))
        print("  Greed:      " + str(self.greed))
        print("  Sneak:      " + str(self.sneak))
        print("  Plead:      " + str(self.plead))
        print("Defense:      " + str(self.averageDefense()))
        print("  Vigilence:  " + str(self.vigilence))
        print("  Perception: " + str(self.perception))
        print("  Blocking:   " + str(self.blocking))
        print("  Chasing:    " + str(self.chasing))


class Team:
    
    pAmount = 5
    bAmount = 8

    def __init__(self, name = "Hades Tigers", slogan = "Never Look Back", symbol = "$"):
        self.name = name
        self.slogan = slogan
        self.symbol = symbol
        self.wins = 0
        self.losses = 0
        self.games = 0
        self.championships = 0 #possibly will go unused
        self.currentPitcher = 0 # zero indexed
        self.pitchers = []
        for i in range(0, self.pAmount):
            self.pitchers.append(Player(genfname(i), genlname(0), -1))
        self.batters = []
        for i in range(0, self.bAmount):
            self.batters.append(Player(genfname(i), genlname(1), i))

    def record(self):
        return str(self.wins) + "-" + str(self.losses)

    def __str__(self):
        return self.name + " " + self.symbol + ", \"" + self.slogan + "\" " + self.record()
    
    def listPlayers(self):
        print("Pitchers:")
        for pitcher in self.pitchers:
            print("  " + str(pitcher))
        print("Batters:")
        for batter in self.batters:
            print("  " + str(batter))

    def promptPlayers(self):
        count = 1
        print("Pitchers:")
        for pitcher in self.pitchers:
            print(str(count) + ")" + (" " * (3 - len(str(count)))) + str(pitcher))
            count = count + 1
        print("Batters:")
        for batter in self.batters:
            print(str(count) + ")" + (" " * (3 - len(str(count)))) + str(batter))
            count = count + 1

    def getPlayer(self, number):
        number = number - 1
        if number > len(self.batters) + len(self.pitchers) or number < 0:
            raise Exception("Input out of range")
        elif number > len(self.pitchers):
            return self.batters[number-len(self.pitchers)]
        else:
            return self.pitchers[number]
        
    def getCurrentPitcher(self):
        return self.pitchers[self.currentPitcher]
    
    def win(self):
        self.wins = self.wins + 1
        self.games = self.games + 1
        self.currentPitcher = (self.currentPitcher + 1) % len(self.pitchers)

    def lose(self):
        self.losses = self.losses + 1
        self.games = self.games + 1
        self.currentPitcher = (self.currentPitcher + 1) % len(self.pitchers)

    def displayDetail(self, prompt = False):
        print(self.name + " " + self.symbol)
        print("\""+self.slogan+"\"")
        print("Wins:          " + str(self.wins))
        print("Losses:        " + str(self.losses))
        print("Games Played:  " + str(self.games))
        print("Championships: " + str(self.championships))
        if prompt:
            self.promptPlayers()
        else:
            self.listPlayers()

