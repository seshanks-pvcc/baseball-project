# baseball-project
This is my final project for CSC221. It will simulate a game of baseball. It is loosely based off of the logic of Blaseball (RIV.) To run the program run baseball.py and use the text based interface to either look at a team and its players or to start a game between two teams.

### Baseball overview
In case you are unfamiliar with the game of baseball it is a ball-and-bat game that is playing in an area with four "Bases" layed out in a diamond. Visiting all four bases earns a player a point known as a "Run." Over the course of 9 "Innings" two teams take turns "Batting" and "Pitching" in order to attempt to earn Runs or prevent the opposing team from earning Runs, respectively. Each Inning is split into a "Top half" and a "Bottom half," which end after the Batting team receives three "Outs," earned either by players getting tagged by the ball while running between bases, or receiving three "Strikes" when they fail to hit a pitched ball that was within the "Strike Zone," an area where the ball is supposed to be hittable. After a team gets three Outs the next Half-Inning occurs and the other team gets their chance to Bat. 
While Batting, a team sends their players one by one to Bat, where they stand over a certain base designated "Home Plate," and attempt to hit the balls thrown at them by a player on the opposing team known as the Pitcher. As mentioned, if these balls are thrown towards the "Strike Zone" and the Batter fails to hit, or if the Batter swings at any ball and does not hit it, it the Batter receives a Strike. Upon receiving three Strikes a Batter "Strikes out" and the next player on the Batting team steps up to the plate. If the ball is thrown outside the Strike Zone and the Batter does not swing at it the Batter receives a "Ball." Upon receiving the fourth Ball, the Batter gets to advance to the First Base unimpeded, causing players on the bases to advance to make room if necessary. If the Batter hits the ball they either hit it towards the field into play, or away from the field, making it a "Foul Ball," which causes the Batter to receive a Strike unless it would cause them to Strikeout. If the ball is valid it can be caught out of the air by a player on the Pitching team to get the Batter Out immeadiately, or it can go beyond the confines of the field while remaining in play, in which case it will be a "Home Run," meaning the the Batter and all players on Base get to go Home, earning one Run each. If the ball is not hit into either of those situations, the Batter (and players on Base) must run the Bases, attempting to make as much progress as possible before the opposing team can grab the ball and tag or threaten to tag the running players. 
While Pitching, a teams players stand out in the field in specific Positions in order to catch and transport balls that are hit into play, as well as the Pitcher, who stands in the middle of the bases and throws the ball at the Batter.

## Interface
The user will interface with the program through a basic text based interface. The user will be presented with a choice in the form:
```
1) Choice 1
2) Choice 2
X) Choice X
99) End
```
The user will input a number and their choice will be fed into code structure (either if/elif/else or match/case) and depending on their choice a function will be run or information will be recorded. If the user selects "99) End" they will be sent back to the main menu or the program will end if they are already in the main menu. The main menu is a while loop whose condition is only set to false if the user selects End on it. This is already implemented.

## Teams
Team will be a class consisting of a list of `Pitchers` (length 5 by default) and `Batters` (length 8 by default) both of which are lists of Player objects, and other attributes recording information such a name and win/loss record. The full list of attributes will be as follows:
```
#Attribute     Type
name           str
slogan         str
symbol         str (single character)
wins           int
losses         int
games          int
championships  int (for compatibility with future/advanced versions that might be implemented after the basic game is)
currentPitcher int
pitchers       list of Players (default length 5)
batters        list of Players (default length 8)
```
Teams will also have a number of methods to define how they are displayed, as well as grabbing the current pitcher, and incrementing wins or losses.

## Players
Player will be a class consisting of a number of statistical attributes which will affect the odds of the randomly generated rolls as well as a name and position. The list of atributes is as follows:
```
#Attribute       Type
fname            str (Randomly chosen from the first names of players in the BaseballProspectus database retrieved from https://legacy.baseballprospectus.com/sortable/playerid_list.php)
lname            str (Randomly chosen from the last names from the same)
position         str (might be enum to make it easier to implement)

#all of these are floats between 0 and 1
#batting stats
power            (affects the amount of bases that can be run off of a hit (by affecting how far the ball goes))
appraisal        (affects swinging at balls/strikes)
accuracy         (affects foul/fair balls)
twitch           (affects the chance of hitting on swing)

#pitching stats
strength         (counters twitch)
trickiness       (counters appraisal)
resilience       (counters power)
perfection       (affects strike chance)

#baserunning stats
speed            (affects the ability of players to run without being caught)
greed            (affects how often the player attempts to steal)
sneak            (counters vigilence)
plead            (affects advance on outs)

#defense stats
vigilence        (catching base stealers)
perception       (catching hits)
blocking         (prevents runners from advancing)
chasing          (prevents batter from reaching extra bases)
```
The name lists are stored in two separate single collumn "csv" files that in practice are just separated by newlines. The only cleaning I did was remove duplicate names, I didn't even remove the collumn headers. This is because it is funny if a player is named "FIRSTNAME" or "1b"

## Game
The game logic is contained in a single function called runGame() which takes a list of two teams as input (the first team being the away team). The function has local variables that keep track of the players on base, the score, the inning (as a 0-indexed half-inning count), the count of balls/strikes/outs, and which teams are playing. It also has an inner function, output(), which takes a string and outputs in the following format: (although unreasonably large scores in unreasonably long games will break)
```
                                                         |    Bug    |
Sample events, Wyatt Mason hits a ground out to thomas    ^12  XXX-YYY
english. this is the input string                         A@H  B:○●●
                                                           M   S:●●
                                                          * *  O:○●
----------------------------------------------------------------------
```
(where A is the away team's symbol, H is the home teams symbol, M is the runner on 2nd's last initial, XXX the away teams's score, YYY the home teams scores, 12 the inning, the ^ signifying the top of the inning (v if the bottom) and the B, S, and O counts showing the count of balls, strikes, and outs respectively.)

As there are many repeating sequences of actions, the game is implemented in a series of nested loops. The largest loop continues as long as the game is running and loops every inning, checking at the end whether the game is supposed to continue.
```
while game is running:
    keep track of which team is pitching and which is batting
    reset the batter count
    announce the start of the half inning and the pitcher
    [Plate appearence logic]
    if the scores are tied or it isn't the bottom of the 9th inning yet and the game isn't already won (by the team that scores in the bottom already being ahead):
        reset the field and count and increase the inning count
    else:
        end the game
```
The next biggest loop runs as long as there are less than three outs and loops every time a player goes up to bat.
```
while there are less than 3 outs:
    reset the ball and strike count
    get the player with the current batter count, store them, and announce them
    [pitch logic]
    increase the batter count
```
The final loop is the most complicated and loops every pitch (unless a runner steals a base) until the batter leaves the plate either through getting on base or getting out.
```
while batter at plate:
    keep track of the events and how many runs are scored this play
    for every runner on 1st or 2nd base, in reverse numerical order:
        check if they can and want to steal (greed) and no one else is stealing and note this
    if a player is trying to steal:
        check if they get caught (runner sneak vs pitcher vigilence) if no:
            advance to the next base and record this to output
        else (caught):
            get out and record this to output
        check if that brought the out count above 3 and end the loop if so
    else (no thief):
        check if the pitch is in the strike zone (pitcher trickiness vs batter appraisal) record this\
        check if the batter swings at the ball (depends of the pitch, out of the zone pitches have the stats reversed)
        if the batter swings:
            check if the batter makes contact with the ball (pitcher strength vs batter twitch, easier if pitch in zone) record this
        if the batter does not make contact:
            increase balls if the pitch is outside the zone and strikes if its inside the zone (record output)
        else (contact):
            check if the ball is fair (batter accuracy)
            fair:
                prevent the batter from batting again
                generate a abstract distance the ball goes (pitcher resilience vs batter power)
                pick a random batter on the pitching team to defend 
                check if the defender can catch the ball
                no:
                    check how many bases the batter can run (abstract distance value + batter speed vs defender chasing) and store it (for output and for next part)
                    for all of the players on base (in reverse numerical order):
                        if its a home run get scored
                        otherwise check if caught while running (runner speed vs defender blocking)
                        no:
                            advance as much as the batter, score if necessary
                        yes:
                            get out (add to output message)
                    if it is a home run the batter scores
                    otherwise they go to the base they reached
                yes (defender caught ball):
                    if the defenders stats caused it to get caught store as a fly out for output otherwise store as ground out
                    for every runner on base (in reverse order):
                        check if advance on the sacrifice (plead vs blocking)
                        yes:
                            advance one base (score if necessary)
                        no:
                            get out
                        (all outcomes are added to the output)
                    add an out
            foul:
                if there are less than two strikes:
                    ass a strike
                store an output message
            if runs were scored that play:
                add the amount to the output message
            output the output message

            if the batter is still batting and there are 3 or more strikes:
                output strikeout message and get batter out (ending batter)
            else if the batter is still batter and there are 4 or more balls:
                output walk and the batter goes to first base displacing runners as necessary (and scoring if bases loaded (which is added to the walk message))
```
That's the extent of the game logic. Every time theres a "check ... (statA vs statB)" in the pseudo code that represents a random number between 0 and 1 being generated is subtracted from by one of the stats (usually with a multiplier) and being compared to a fixed number that is added to by the other stat (also usually with a multiplier.) Lower values lead to favorable outcomes for the batting team. 