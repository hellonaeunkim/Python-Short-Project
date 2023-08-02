from art import logo
from replit import clear
import random


def guess_game(attempts):
  random_num = random.randint(0, 100)
  for i in range(attempts + 1):
      print("You have " + str(attempts) +
            " attempts remaining to guess the number.")
      attempts -= 1
      guess_num = int(input("Make a guess : "))
      if random_num == guess_num:
          print(f"You got it! The answer was {random_num}")
          return
      elif attempts == 0:
          print("You've run out of guesses, you lose.")
          return
      elif random_num < guess_num:
          print("Too high.")
          print("Guess again.")
      elif random_num > guess_num:
          print("Too low.")
          print("Guess again.")


def game_start():
  clear()
  print(logo)

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  level = input("Choose a difficulty. Type 'easy' or 'hard' : ")

  if level == 'easy':
      guess_game(10)
  elif level == 'hard':
      guess_game(5)


game_start()
