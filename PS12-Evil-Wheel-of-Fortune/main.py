import random

def clear():
  print("\033c", end="")

def getGuess():
  while True:
    guess = input("Enter a guess: ").lower().strip()
    if guess in previousGuesses:
      print("You already guessed that! Try again!")
    elif not guess.isalpha():
      print("That's not a letter! Try again!")
    elif len(guess) != 1:
      print("You typed too much, or nothing at all! Try again!")
    else:
      return guess

def getGroups(letter, words):
  wordGroups = {}
  for word in words:
    pattern = getPattern(letter, word)
    if pattern in wordGroups:
      wordGroups[pattern].add(word)
    else:
      wordGroups[pattern] = set({word})
  return wordGroups

def getPattern(letter, word):
  pattern = ""
  for c in word:
    if c == letter or c in correctGuesses:
      pattern += c
    else:
      pattern += "_"
    pattern += " "
  return pattern

def getMaxPattern(wordGroups):
  maxGroupSize = 0
  maxPatterns = []
  for pattern in wordGroups:
    if len(wordGroups[pattern]) > maxGroupSize:
      maxGroupSize = len(wordGroups[pattern])
      maxPatterns = []
      maxPatterns.append(pattern)
    elif len(wordGroups[pattern]) == maxGroupSize:
      maxPatterns.append(pattern)
  return random.choice(maxPatterns)

def getWordsOfLength(length, words):
  temp = set()
  for word in words:
    if len(word) == length:
      temp.add(word)
  return temp
#-----------------------------------------------------

with open("dictionary.txt") as f:
  words = set(f.read().strip().split("\n"))

length = random.randint(3, 8)
status = "_ " * length

words = getWordsOfLength(length, words)

correctGuesses = set()
previousGuesses = []
numGuesses = 15

while True: 
  clear()
  print(status+"\n")
  print(str(numGuesses) + " guesses left!")
  print("Previous Guesses: " + " ".join(previousGuesses))

  guess = getGuess()
  previousGuesses.append(guess)

  # choose the worst case scenario (that's still possible)
  wordGroups = getGroups(guess, words)
  newStatus = getMaxPattern(wordGroups)

  # update words and status
  words = wordGroups[newStatus]
  if newStatus == status: # "incorrect guess"
    # the worst case (that's still possible) is to not reveal any letters!
    numGuesses -= 1
  else: # "correct guess"
    # the worst case (that's still possible) is to reveal letters...
    correctGuesses.add(guess)
    status = newStatus

  if "_" not in status:
    print("\nYOU WIN!\nThe word was: "+list(words)[0])
    break
  elif numGuesses == 0:
    print("\nYOU LOSE!\nThe word was: "+random.choice(list(words)))
    break