import random
import time

pet = {}
pet["happy"] ='''
/\___/\\
\ ^_^ /
`-.U.-'
  /"\\'''
pet["neutral"] ='''
/\___/\\
\ ._. /
`-. .-'
  /"\\'''
pet["sad"] ='''
/\___/\\
\ O_O /
`-.^.-'
  /"\\'''
pet["dead"]='''
/\___/\\
\ X_X /
`-.U.-'
  /"\\'''

def clear():
  print("\033[2J\033[1;1H", end="")

def getNumChoice(message, numChoices):
  while True:
    choice = input(message)
    if choice.isdigit() and int(choice)-1 in range(numChoices):
      return int(choice)

def getDictChoice(message, dictionary):
  while True:
    choice = input(message)
    if choice in dictionary:
      return choice

def feed():
  print("\nOptions:")
  for food in foods:
    print("- "+food)
  print()
  choice = getDictChoice("What food do you want? ", foods)
  print("You fed your pet a "+ choice +"!")
  time.sleep(1)

  if HP > 80:
    print("Your pet is full!") 
    time.sleep(1)
    print("+1 HP")
    return 1
  elif HP < 50:
    print("Your pet is hungry!") 
    time.sleep(1)
    print("+"+ str(foods[choice]*2) +" HP")
    return foods[choice]*2
  else:
    print("+"+ str(foods[choice]) +" HP")
    return foods[choice]

def walk():
  print("You walked your pet!")  
  time.sleep(1)
  if HP > 80:
    print("Your pet is full and that makes walking harder!") 
    time.sleep(1)
    print("+5 HP")
    return 5
  elif HP < 50:
    print("Your pet is hungry and that makes walking harder!") 
    time.sleep(1)
    print("+5 HP")
    return 5
  else:
    print("+20 HP")
    return 20

def play():
  print("You played with your pet!")
  time.sleep(1)
  print("+9 HP")
  return 9

def printPet():
  clear()
  print("HP:",HP)
  if HP == 0:
    print(pet["dead"])
  elif HP < 40:
    print(pet["sad"])
  elif HP < 80:
    print(pet["neutral"])
  elif HP >= 80:
    print(pet["happy"])

HP = 100
round = 1
foods = {"cake":1, "doughnut": 5, "cupcake":15, "muffin":5}

while HP > 0:

  printPet()

  # choices
  if round % 4 == 0:
    print("\n1. Feed\n2. Walk\n3. Play\n4. Nothing\n")
    choice = getNumChoice("What would you like to do? ", 4)
    if choice == 1:
      HP += feed()
    elif choice == 2:
      HP += walk()
    elif choice == 3:
      HP += play()
    elif choice == 4:
      print("You did nothing...")
    if HP >= 100:
      HP = 100

  # decrease HP
  HP -= random.randint(0,5)
  if HP < 0:
    HP = 0
  round += 1
  time.sleep(1)

printPet()
