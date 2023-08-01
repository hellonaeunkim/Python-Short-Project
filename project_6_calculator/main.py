#Calculator

from replit import clear
from art import logo

#Add
def add(a, b):
  return a + b

#Subtract
def subtract(a, b):
  return a - b

#Multiply
def multiply(a, b):
  return a * b

#Divide
def divide(a, b):
  return a / b

#Dictionary
operations = {
  "+": add,
  "-": subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number? : "))

  ask_continue = "y"
  while ask_continue == "y":
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the line above : ")
    num2 = float(input("What's the next number? : "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)                        
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    ask_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    num1 = answer

  clear()
  calculator()

calculator()
  











#Before editing

# ask_continue = "n"
# while ask_continue == "n":
#   clear()
#   first_num = int(input("What's the first number? : "))
#   for symbol in operations:
#     print(symbol)
#   operation_symbol = input("Pick an operation from the line above : ")
#   second_num = int(input("What's the next number? : "))
#   calculation_function = operations[operation_symbol]
#   first_answer = calculation_function(first_num, second_num)
#   print(f"{first_num} {operation_symbol} {second_num} = {first_answer}")
  
#   ask_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: ")

# beginning_answer = first_answer
# while ask_continue == "y":
#   for symbol in operations:
#     print(symbol)
#   operation_symbol = input("Pick an operation from the line above : ")
#   next_num = int(input("What's the next number? : "))
#   calculation_function = operations[operation_symbol]
#   answer = calculation_function(beginning_answer, next_num)
#   print(f"{beginning_answer} {operation_symbol} {next_num} = {answer}")
  
#   ask_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
#   beginning_answer = answer
 
  