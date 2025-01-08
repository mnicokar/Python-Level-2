import random
import time

def loadTrivia():
  questions, answers = [], []
  with open("trivia.txt") as f:
    lines = f.read().strip().split("\n")
    for line in lines:
      if "Trivia Question:" in line:
        questions.append(line.replace("Trivia Question:", '') .strip())
      elif "Answer:" in line:
        answers.append(line.replace("Answer:", '').strip())
  return dict(zip(questions, answers))

def clear():
  print("\033[2J\033[1;1;H", end="")

trivia = loadTrivia()
questions = []
for question in trivia:
  questions.append(question)

RULES = '''Welcome to Trivia Master!

You score 100 points for every correctly guessed question!
You can have as many players and questions as you want!
'''
print(RULES)
input("Press enter to start!")
clear()

# add all the players!
numPlayers = 0
while True:
  numPlayers = input("How many players will be playing? ")
  if numPlayers.isdigit() and int(numPlayers) > 0:
    numPlayers = int(numPlayers)
    break
players = {}
for i in range(numPlayers):
  name = input("Enter the name of player " + str(i+1) + ": ")
  players[name] = 0

# determine the number of questions
numQuestions = 0
while True:
  numQuestions = input("How many questions do you want total? ")
  if numQuestions.isdigit() and int(numQuestions) > 0:
    numQuestions = int(numQuestions)
    if numQuestions > len(questions):
      print("Sorry! There are only "+str(len(questions)) + " questions. We'll make sure we ask you everything we have!")
      numQuestions = len(questions)
      time.sleep(4)
    break

# play the game!
questionsAnswered = 0
while True:
  for player in players:
    clear()
    print(player + "'s turn! ", end="")
    print(str(questionsAnswered+1) + "/" + str(numQuestions))
    print("Your current score is: " + str(players[player]))

    question = random.choice(questions)
    print("\n"+question)
    answer = input().strip()

    if answer.lower() == trivia[question].lower():
      print("\nCorrect! You win 100 points!")
      players[player] += 100
      questions.remove(question)
    else:
      print("\nIncorrect! Better luck next time!")
      print("The correct answer was: " + trivia[question])
    questionsAnswered += 1
    time.sleep(4)
    
    if questionsAnswered == numQuestions:
      break
  if questionsAnswered == numQuestions:
      clear()
      print("You've been asked all " + str(numQuestions) + " questions!")
      break
  
# determine the winners!
highestScore = 0
winners = []
for player in players:
  if players[player] > highestScore:
    winners = []
    winners.append(player)
    highestScore = players[player]
  elif players[player] == highestScore:
    winners.append(player)

# print winners
print()
if len(winners) == 1:
  print(winners[0] + " WINS!")
else:
  print("It was a " + str(len(winners)) + "-way tie!")
  print("Here are the winners: ")
  for player in winners:
    print(player)

#print final scores
print("\nHere are all the final scores:")
for player in players:
  print(player + ": " + str(players[player]))
