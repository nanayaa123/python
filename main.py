#Khalid #Naya
print("WELCOME TO MY ADVENTURE GAME!")

name = input("Enter name of player: " )
print("Welcome " + name + ". In order to win this game you must make good choices! ")

start = input("Would you like to begin playing? (yes/no)")
if start == "yes":
  print("YAAAAAYYYYYY!!! Let's begin the adventure.")
  answer1 = input("Ana hears a loud noise in the middle of the night while she is sleeping. Should she go check what is going on or continue to sleep? (go/stay)")
elif start == "no":
  print("Lame. You lost too early :( ")
  quit()

else:
  print("Invalid choice! You lost.")
  quit()
if answer1 == "go":
  print("Good choice!! You're doing great")
elif answer1 == "stay":
  print("Wrong choice. You lost")
  quit()
else:
  print("Invalid choice")
  quit()

answer2 = input("In the main hall she finds a teddy bear which does not belong to her. She wants to pick it up. Should she pick it up or leave it? (pick it/leave it)")

if answer2 == "pick it":
  print("That's a good choice!")

elif answer2 == "leave it":
  print("Wrong choice! You lost :( ")
  quit()

else:
  print("Invalid choice. You lost!")
  quit()

answer3 = input(" The moment Ana picks the teddy bear up the teddy bear starts to talk and tells her she is in great danger and there is a monster in her house. The monster had caputured her PARENTS as well!!! The teddy bear tells her not to get scared and he knows how to beat the monster.The teddy bear pulls out a magic potion and asks Ana to take it. He tells her the potion will weaken the monster and kill it.Should she take it? (yes/no)")

if answer3 == "yes":
  print("You are pretty good at this game. Keep on going!")

elif answer3 == "no":
  print("Wrong choice. You lost!")
  quit()

else:
  print("Invalid choice. You lost!")
  quit()

answer4 = input("Ana runs down the road and sees her parents tied to a tree. Should she untie them or leave them to suffer? (untie them/ leave them)")

if answer4 == "untie them":
  print("GREAT IDEA!")

elif answer4 == "leave them":
  print("Wrong choice. You lost :(")
  quit()

else:
  print("Invalid choice. You lost")
  quit()

answer5 = input("Ana starts running around the house looking for the MONSTER to scare him away. She finally comes to meet the MONSTER face-to-face eating food from the kitchen. The MONSTER has a knife in his hand. What should Ana do right now? (use the potion/ run away) ")

if answer5 == "use the potion":
  print("Congratulations you have successfully killed the MONSTER. YOU WON!!! ")

elif answer5 == "run away":
  print("You are not brave! You lost :(")
  quit()

else:
  print("Invalid choice! ")
  print(" End of the game:( ")
  print("    YOU LOST!")
  quit()
  
     

