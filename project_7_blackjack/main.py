############### This Blackjack Game Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

############ The Blackjack Game Code by Na-Eun Kim ############

from replit import clear
from art import logo
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card

def calculate_score(cards):
  if sum(cards) > 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    list.remove(11)
    list.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    print("You went over. You lose 😭")
  
  if user_score == computer_score:
    print("Draw 🙃")
  elif computer_score == 0:
    print("Lose, opponent has Blackjack 😱")
  elif user_score == 0:
    print("Win with a Blackjack 😎")
  elif user_score > 21:
    print("You went over. You lose 😭")
  elif computer_score > 21:
    print("Opponent went over. You win 😁")
  elif user_score > computer_score:
    print("You win 😃")
  else:
    print("You lose 😤")

def blackjack():

  print(logo)

  user_cards = []
  computer_cards = []
  game_end = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while not game_end:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_end = True
    else:
      draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
      if draw_again == "y":
        user_cards.append(deal_card())
      else:
        game_end = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  blackjack()
  