import random
import copy
import time

def clear():
  print("\033c", end="")

def rollAnimation():
  msg = "Rolling"
  print()
  for i in range(4):
    print(msg)
    time.sleep(0.5)
    print("\033[2A\033[2K")
    msg += "."
  
  print("\033[2K\033[2A")

def rollDice(numDice):
  rollAnimation()
  dice = []
  for i in range(numDice):
    dice.append(random.randint(1, 6))
  return dice

def printDice(dice):
  print("\033[1m")
  for die in dice:
    print(die, end=" ")
  print("\n\033[m")

def multiples(choices):
  target = int(choices[0])
  for die in choices:
    die = int(die)
    if die != target:
      return 0
  if len(choices) == 3:
    if target == 1:
      return 300
    else:
      return int(target)*100
  elif len(choices) == 4:
    return 1000
  elif len(choices) == 5:
    return 2000
  elif len(choices) == 6:
    return 3000
  return 0

def getScore(choices):
  score = 0
  for die in choices:
    if die == "1":
      score += 100
    elif die == "5":
      score += 50
    else:
      return 0
  return score

def validChoices(choices, dice):
  dice_copy = copy.copy(dice)
  for choice in choices:
    if not choice.isdigit():
      return False
    elif int(choice) not in dice_copy:
      return False
    elif int(choice) != 1 and int(choice) != 5:
      return False
    dice_copy.remove(int(choice))
  for choice in choices:
    dice.remove(int(choice))
  return True

def goodRoll():
  global dice, roundScore
  dice = rollDice(len(dice))
  printDice(dice)

  if 1 not in dice and 5 not in dice:
    print("FARKLE!\nYou didn't roll any 1's or 5's!\nYou lose all your points for the round!")
    time.sleep(1)
    roundScore = 0
    return False

  while True:
    choices = input("What dice do you want to keep? ").strip().split(" ")
    if validChoices(choices, dice):
      newScore = getScore(choices)
      roundScore += newScore
      print("You scored " + str(newScore) + " points!")
      if len(dice) == 0:
        print("WOOHOO! You get all the dice back!")
        dice = [1, 2, 3, 4, 5, 6]
      return True

def rollAgain():
  gameState = ""
  while True:
    gameState = input("Roll Again? (y/n) ").lower()
    if gameState == "y":
     return True
    elif gameState == "n":
      return False

def takeATurn():
  global dice, roundScore
  dice = [1, 2, 3, 4, 5, 6]
  roundScore = 0
  while True:
    if goodRoll():
      if not rollAgain():
        return roundScore
    else:
      return roundScore


RULES = '''--------------------
      FARKLE!
--------------------

Be the first to reach 1000 points!
If you roll a 1 or a 5 you can keep it. 

1 = 100 points
5 = 50 points

Keep as many 1s and 5s as you want.
But you have to keep at least one... or you farkle!
'''
print(RULES)
input("Press Enter to Start!")
clear()
    
p1Score = 0
p2Score = 0

while True:

  print("P1 Score:", p1Score)
  p1Score += takeATurn()
  print("\nP1 Score:", p1Score)
  if p1Score >= 1000:
    print("\nP1 WINS!")
    break
  time.sleep(3)
  clear()

  print("P2 Score:", p2Score)
  p2Score += takeATurn()
  print("\nP2 Score:", p2Score)
  if p2Score >= 1000:
    print("\nP2 WINS!")
    break
  time.sleep(3)
  clear()


print("Final Scores:")
print("P1 Score:", p1Score)
print("P2 Score:", p2Score)