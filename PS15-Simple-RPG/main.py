import time

def clear():
  print("\033c", end="")

def getMove():
  moves = ["attack", "shield", "heal", "powerup"]
  print("\nMoves:")
  for move in moves:
    print(" - " + move)
  print()
  while True:
    move = input("What do you do? ")
    if move in moves:
      return move
  print("\n")

def playerMove(move):
  if move == "attack":
    if roundNum % 3 == 2 :
      print("Your attack does twice the damage! (" + str(player["Attack"]*2) + "HP)")
      time.sleep(1)
      enemy["HP"] -= player["Attack"]*2
    else:
      print("You attacked the enemy! ("+ str(player["Attack"]) + "HP)")
      enemy["HP"] -= player["Attack"]
  elif move == "shield":
    if player["Shield"] == "Broken":
      print("You can't use your shield because it's still being fixed!")
    else:
      print("You put up your shield!")
      player["Shield"] = "Up"
  elif move == "heal":
    print("You healed yourself! +15 HP")
    player["HP"] = min(player["HP"]+15, 100)
  elif move == "powerup":
    print("You powered up! +5 Attack")
    player["Attack"] = min(player["Attack"]+5, 50)
  
  if player["Shield"] == "Broken":
    player["Shield"] = "Down"
  time.sleep(1)

def enemyAttack():
  if not player["Shield"] == "Up":
      player["HP"] -= enemy["Attack"]
      print("-" + str(enemy["Attack"]) + "HP")
  else:
    print("Your shield kept you safe, but it was destroyed!")
    player["Shield"] = "Broken"

def enemyMove():
  cycle = roundNum % 3
  if cycle == 0:
    print("The enemy attacked! ")
    time.sleep(1)
    enemyAttack()
  elif cycle == 1:
    print("The enemy powered up!\nHe's REALLY powerful now! (but more vulnerable)")
    time.sleep(1)
    enemy["Attack"] += 2
    enemy["Attack"] *= 2
  elif cycle == 2:
    print("The enemy performed a SUPER-ULTRA-MEGA attack! ")
    time.sleep(1)
    enemyAttack()
    enemy["Attack"] = int(enemy["Attack"]/2)
  time.sleep(2)

def printStats():  
  print("YOU:  ", player["HP"],end="")
  if player["Shield"] == "Up":
    print(' (Shield)')
  else:
    print()
  print("ENEMY:", enemy["HP"])


#-------------------------------------------------

roundNum = 0
player = {"HP":100, "Attack":5, "Shield":"Down"}
enemy = {"HP":100, "Attack":15}

print("An enemy appeared!")
time.sleep(2)
clear()

while True:
  printStats()
  playerMove(getMove())
  enemyMove()

  if player["HP"] <= 0:
    print("\nYou were destroyed :(")
    break
  elif enemy["HP"] <= 0:
    print("\nYOU WIN!\nYOU CONQUERED THE ENEMY!")
    break

  roundNum += 1
  clear()

# shield only once per cycle
# no more than 