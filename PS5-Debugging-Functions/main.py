# Your friend, Kant D. Bugg, is learning how to use functions and wrote a script to play a guessing game against the computer. Unfortunately, his script has some bugs in it. Help Kant find the bugs and get his script running!

# Each time you run the code, read the error messages in the console. Each message will tell you which line to look for a bug, and even give you a hint about what the bug is.

# After you find and fix the bug, run the code again. Read the new error message and find the next bug, until the program runs fully!

# If you can't remember how to fix a certain line of code, look at one of your past projects for an example.

import random

def printWelcome()
  print("I am thinking of a random number between 1 and 100. Guess what it is!")


# Get my secret number between 1 and 100!
def getRandomNumber():
  myRandomNumber = random.randint(0,100)
  return myRandomNumber


# Ask the user to guess my secret number
def getGuessFromUser:
  guess = int(input("Enter a new guess: "))
  return guess


# If the guess is correct, then return True. Otherwise, print out if the guess was too high or too low, and return False
def answerIsRight(answer, guess):
  if answer == guess:
    return "True"
  elif guess < answer:
    print("You guessed too low!")
    return "False"
  else:
    print("You guessed too high!")
    return "False"


def printScore():
  print('It took you ' + str(numGuesses) + ' guesses to guess my number.')
  if numGuesses == 1:
    print("Lucky you, you guessed my secret number on the first try!")
  elif numGuesses < 5:
    print("Pretty solid guessing, it took you less than 5 tries to guess my number!")
  elif numGuesses < 15:
    print("Pretty average guessing!")
  else:
    print("Wow, it took you forever to guess my number!")


def playGame()
  printWelcome
  answer = getRandomNumber(0,100)

  # Ask the user to guess the secret number, then check if they got it right. If they didn't get it right, let them keep guessing until they guess correctly!
  guess = getGuessFromUser()
  numGuesses = 1 # Count how many guesses it took for the user to guess the number
  while not answerIsRight(answer, getGuessFromUser()):
    guess = getGuessFromUser()
    numGuesses = numGuesses + 1

  printScore()

playGame()

# Bonus: Allow the user type in Y or N at the end of each game to decide whether or not to play again.