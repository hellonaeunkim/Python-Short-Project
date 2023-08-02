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

pick = [rock, paper, scissors]

random_num = random.randint(0,2)

user = int(input("Pick one! Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if 0 <= user < len(pick):
  print("\n Your choose : \n " + pick[user])
  print("\n Computer choose : \n " + pick[random_num])
  if user == random_num:
    print("Tied. Let's try again!")
  elif user < random_num:
    if user == 0 and random_num == 2:
      print("You win!")
    else:
      print("You loose!")
  elif user > random_num:
    if user == 2 and random_num == 0:
      print("You loose!")
    else:
      print("You win!")
else:
  print("\n You typed invalid number, try again.")
