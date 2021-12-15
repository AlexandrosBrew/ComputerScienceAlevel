'''Laser Tag is a game where teams of players move round an arena shooting each other with infrared guns. Players wear sensors that keep track of how many times they have been hit by the laser. This is known as being ‘tagged’.

At the end of each match players upload their score to a computer. The computer stores the scores in the order they are received in a 2D array called player. The array stores the team as an integer (1 for green, 2 for red) and their score. An extract of the array called  is shown below. The first entry shows a green team member scored 45 points and the next shows a red team member scored 30 points.


1	45
2	30
2	46
1	31
1	10
1	32
2	2
 
Once all the players have uploaded their scores the computer adds up the scores for each team.

Using pseudocode write a program for a procedural language that works out and outputs the total score for each team. You may assume that there are always 20 players.
'''
from random import *
player = []

for i in range(20):
  # code to randomly assign a team and player to each player
  team = randint(1,2)
  score = randint(5, 50)
  player.append([team, score])

for item in player:
  print(item)


# write your answer here...  
# Assume that you have a 2D array called player with
# 20 rows (each row is the data for 1 player)
total1 = 0
total2 = 0
for i in range(len(player)):
	if player[i][0] == 1:
		total1+= player[i][1]
	elif player[i][0] == 2:
		total2 += player[i][2]
print("The total score of team 1 is: "+total1)
print("The total score of team 2 is: "+total2)