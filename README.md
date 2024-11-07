# baseball-project
This is my final project for CSC221. It will simulate a game of baseball.

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
99) End```
The user will input a number and their choice will be fed into code structure (either if/elif/else or match/case) and depending on their choice a function will be run or information will be recorded. If the user selects "99) End" they will be sent back to the main menu or the program will end if they are already in the main menu. The main menu is a while loop whose condition is only set to false if the user selects End on it. This is already implemented.

## Teams
Team will be a class consisting of a list of `Pitchers` and `Batters` both of which are lists of Player objects, and other attributes recording information such a name and win/loss record

## Players
Player will be a class consisting of a number of statistical attributes which will affect the odds of the randomly generated rolls as well as a name.
