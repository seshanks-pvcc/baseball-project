#Team.py
import random 

#Converts a value from 0 to 1 to a str of stars from 0 stars to 5 stars 
def toStars(stat):
    return ("☆","★")[stat >= 0.2] + ("☆","★")[stat >= 0.4] + ("☆","★")[stat >= 0.6] + ("☆","★")[stat >= 0.8] + ("☆","★")[stat >= 1]

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
        return self.fname + " " + self.lname + ", " + self.getPosition() + ": " + toStars((self.averageBatting(), self.averagePitching())[self.getPosition() == self.positions[-1]])
    
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
    name = ""
    slogan = ""
    
    wins = 0
    losses = 0
    games = 0
    championships = 0 #possibly will go unused
    currentPitcher = 0 # zero indexed
    pitchers = []
    batters = []
