import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]
userChoise = int(input(" What do you choose? Enter 0 for Rock, type 1 for paper or 2 for Scissors \n"))
print(f"User choise is {userChoise}")
print(game_images[userChoise])


compChoise = random.randint(0,2)
print(f"Computer choise is {compChoise}")

print(game_images[compChoise])
if userChoise>=3 or userChoise<0:
  print("You input an invalid number. you lose!")
elif userChoise == 0 and compChoise == 2:
  print ("You win")
elif compChoise == 0 and userChoise==2:
  print (" Your lose")
elif userChoise>=3 or userChoise<0:
  print("You input an invalid number. you lose!")
elif compChoise > userChoise:
  print("You lose")
elif userChoise>compChoise:
  print("You win")
elif userChoise==compChoise:
  print("It is a draw")