import random
import time

def clear():
  print("\033c", end="")
def getGuess(message):
  while True:
    guess = input(message)
    if guess.isdigit() and 0 <= int(guess) < len(grid):
      return int(guess)

def printGrid(grid):
  print("  ", end="")
  for j in range(len(grid[0])):
    print(str(j), end=" ")
  print()
  for i in range(len(grid)):
    print(i, end = " ")
    for j in range(len(grid[i])):
      print(grid[i][j], end=" ")
    print()

def newGrid(size):
  grid = []
  for i in range(size):
    row = []
    for j in range(size):
      row.append("-")
    grid.append(row)
  return grid

def placeHorizontal(size):
  r = 0
  c = 0
  collision = True
  while collision:
    r = random.randint(0, len(ships)-1)
    c = random.randint(0, len(ships)-size)
    collision = False
    for i in range(size):
      if ships[r][c+i] == "X":
        collision = True
    print()
  for i in range(size):
    ships[r][c+i] = "X"
  return True
def placeVertical(size):
  r = 0
  c = 0
  collision = True
  while collision:
    r = random.randint(0, len(ships)-size)
    c = random.randint(0, len(ships)-1)
    collision = False
    for i in range(size):
      if ships[r+i][c] == "X":
        collision = True
    print()
  for i in range(size):
    ships[r+i][c] = "X"
    
def placeShip(size):
  if random.randint(0,1) == 0:
    placeHorizontal(size)
  else:
    placeVertical(size)
  return size

GRID_SIZE = 6
RULES = '''Welcome to Battleship! 
Sink the two ships by guessing the coordinates!
-2 piece
-3 piece
'''
print(RULES)
input("Press enter to start!")

grid = newGrid(GRID_SIZE)
ships = newGrid(GRID_SIZE)

hitsLeft = 0
hitsLeft += placeShip(2)
hitsLeft += placeShip(3)

while True:
  clear()
  printGrid(grid)
  row = getGuess("\nPick a row: ")
  col = getGuess("Pick a column: ")

  if grid[row][col] != "-":
    print("You already guessed this location!")
  elif ships[row][col] == "X":
    grid[row][col] = "X"
    hitsLeft -= 1
    print("It's a hit!")
  else:
    grid[row][col] = "."
    print("It's a miss!")
  
  time.sleep(1)

  if hitsLeft == 0:
    break

clear()
print("YOU WIN!")
printGrid(grid)