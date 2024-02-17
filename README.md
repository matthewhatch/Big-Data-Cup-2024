# Hypothesis
 There are a few questions we would like to answer.  Here is how we came up with them.

 Since this is Andy's first real exposure to a project like this, I simply asked him what the goal of a hockey game is. "Score more goals than the other team."  Yup!  It's that simple and something we all know, but its worth asking some follow up questions.

 - What is the area of the ice where a player is more likely to score?
 - What is the most affective way to enter the zone to in order to get a player on your team into that area for a shot
 - How often do those shots, based on zone entry type, find the back of the net (turn into goals)
 

 #### Step 1 - Assumuption
 We can make an assumption that the high value shot area is the trapezoid from goal post to goal post and up to the dots.  But we should provide some data to back that up.  Since there is limited data from 4 games we won't state this as fact, but its a good place to start.

 ### Step 2 - Generate new Data set
 What are the Zone Entry types?
 - Carry
 - Dump
 - Play

 Of these 3 methods of entering the offensive zone, which one is most likely to lead to a quality shot?  We should define what we mean by "leads to a quality shot".
 In order for a shot to be attributed to a zone entry, it must happen after the zone entry and before a change in possession.  At this time, a change in possession includes a Dump Out, Pass Play,Face-Off (any play that leads to a face-off), or the end of the period.

 We will collect all Zone Entry Plays and all plays leading up to and including either a Shot, Goal, DumpOout by the opposing team, Pass Play by opposing team, Face-Off, or the end of the period.
- Clock Time - (20:00 is the beginning of the period)
- Period - (1,2,3) Period higher than 3 is OT
- Entry Type - (Carry, Play, Dump)
- Quality Shot (True, False)
- Game Situation (Winning, Losing, Tied)
- Even Stength (True, False)

### Step 3 - Analyze
