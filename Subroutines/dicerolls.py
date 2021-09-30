'''
The function roll() simulates the outcome of one random roll of an n-sided dice. 
E.g. roll() will randomly return either 1,2,3,4,5 or 6.

The code below calls the roll() function and prints the role and continues to do this until a 6 is rolled. The code then displays a message saying how many rolls it took
to get to a 6.
'''
from random import *

def roll():
  r = randint(1,6)
  return r

count = 0
dice = 0
while dice!=6:
  dice = roll()
  print("you rolled a " + str(dice))
  count = count+1

print()
print("You had to roll the dice "+ str(count) + " times to get a six")
