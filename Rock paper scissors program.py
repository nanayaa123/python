import random
print("Rock, Paper or Scissors?\nPlease enter your choice how it is shown below\nRock | Paper | Scissors\n")
user = input("")
rng = random.randint (1,3)

if rng == 1:
  print("Computer chose Rock")
elif rng == 2:
  print("Computer chose Paper")
elif rng == 3:
  print("Computer chose Scissors")
pass

if user == "Rock" and rng == 1:
  print("You Tied")
elif user == "Rock" and rng == 2:
  print("You Lost")
elif user == "Rock" and rng == 3:
  print("You Won!")
pass

if user == "Paper" and rng == 1:
  print("You Won!")
elif user == "Paper" and rng == 2:
  print("You Tied")
elif user == "Paper" and rng == 3:
  print("You Lost")

if user == "Scissors" and rng == 1:
  print("You Lost")
elif user == "Scissors" and rng == 2:
  print("You Won")
elif user == "Scissors" and rng == 3:
  print("You Tied")

