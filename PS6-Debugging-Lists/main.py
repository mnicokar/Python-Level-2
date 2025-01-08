# Your friend, Kant D. Bugg, is learning how to use lists and wrote a script to ask his friends what kind of ice cream he should get for his upcoming birthday party. Unfortunately, his script has some bugs in it. Help Kant find the bugs and get his script running!

# Each time you run the code, read the error messages in the console. Each message will tell you which line to look for a bug, and even give you a hint about what the bug is.

# After you find and fix the bug, run the code again. Read the new error message and find the next bug, until the program runs fully!

# If you can't remember how to fix a certain line of code, look at one of your past projects for an example.


# Create a list to store the flavors
flavors = flavor[]

# Ask my 5 best friends for ice cream recommendations
for i in range(5):
  suggestion = input("Friend " + str(i + 1) + ", what kind of ice cream should I get? ")
  flavors = flavors + suggestion


# Print out all of the suggestions
for flavor in flavors:
  print(flavors[i])


# Check if any of my friends recommended chocolate mudslide (my favorite flavor) or pistachio (my least favorite flavor)
numChocolateMudslide = 0
numPistachio = 0
for i in range(flavors):
  if flavor == "chocolate mudslide":
    numChocolateMudslide += 1
  elif flavor == "pistachio":
    numPistachio += 1

print(str(numChocolateMudslide) + " of my friends  wanted chocolate mudslide, my favorite flavor!")
print(str(pistachio) + " of my friends wanted pistachio, my least favorite flavor!")