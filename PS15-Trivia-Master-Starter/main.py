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

trivia = loadTrivia()
