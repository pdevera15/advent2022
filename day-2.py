# Score
# Rock: 1
# Paper: 2
# Scissor: 3

# Lost: 0
# Draw: 3
# Won: 6

# a = rock, b = paper, c = scissor
# x = rock, y = paper, z = scissor

handScore = {"rock": 1, "paper": 2, "scissor": 3}
score = {"lost": 0, "draw": 3, "won": 6}
handDict = {"A" : "rock", "B": "paper", "C": "scissor", "X" : "rock", "Y": "paper", "Z": "scissor"}
totalScore = 0
with open("day-2-input.txt") as f:
  for line in f:
    p1 = handDict[line.split()[0]]
    p2 = handDict[line.split()[1]]
    
    if (p1 == p2):
      totalScore += handScore[p2] + score["draw"]
    elif p2 == "rock" and p1 == "scissor" or p2 == "paper" and p1 == "rock" or p2 == "scissor" and p1 == "paper":
      totalScore += handScore[p2] + score["won"]
    elif p2 == "rock" and p1 == "paper" or p2 == "paper" and p1 == "scissor" or p2 == "scissor" and p1 == "rock":
      totalScore += handScore[p2] + score["lost"]

print(totalScore)
# Logic Table
# if p2 = p1:
#   draw
# elif p2.rock  p1.paper:
#   lose
# elif p2.rock p1.scissor
#   win
# elif p2.paper p1.rock
#   win
# elif p2.paper p1.scissor
#   lost
# elif p2.Scissor p1.rock
#   lost
# elif p2.scissor p1.paper
#   win