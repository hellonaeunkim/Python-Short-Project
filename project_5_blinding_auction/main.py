from replit import clear
from art import logo

print(logo + "\n")

auction = {}
ask_continue = "yes"

while ask_continue == "yes":
  ask_name = input("Welcome. What is your name? ")
  ask_bid = int(input("What is your bid? $"))
  auction[ask_name] = ask_bid
  ask_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if ask_continue == "yes":
    clear()

highest_bid_key = max(auction)
highest_bid = auction[highest_bid_key]

print(f"The winner is {highest_bid_key} with a bid of ${highest_bid}")

#Using for instead max()

# def max_dictionary():
#   highest_bid = 0 
#   highest_bid_key = ""
#   for key in auction:
#     temp_1 = auction[key]
#     if temp_1 >= highest_bid:
#       highest_bid = temp_1
#       highest_bid_key = key

#   print(f"The winner is {highest_bid_key} with a bid of ${highest_bid}")    
  
# auction = {}
# ask_continue = "yes"

# while ask_continue == "yes":
#   ask_name = input("Welcome. What is your name? ")
#   ask_bid = int(input("What is your bid? $"))
#   auction[ask_name] = ask_bid
#   ask_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if ask_continue == "yes":
#     clear()
#   elif ask_continue == "no":
#     max_dictionary()