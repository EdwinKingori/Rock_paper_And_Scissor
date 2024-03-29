# Learning to use functions, dictionaries and if-else \ nested statements

import random 

def get_choices():
  options = ["Rock", "Paper", "Scissors"]

  while True:
    player_choice = input("Rock,Paper,Scissors...  ").capitalize()
    if player_choice in options:
      break
    else:
      print("Invalid Input! Choose from: Rock, Paper or Scissors")

  computer_choice = random.choice(options)
  # using a dictionary to store key data values in key value pairs
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer):
  print(f"You chose {player}, and Computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "Rock":
    if computer == "Scissors":
      return "Rock smashes Scissors, You win! bloody hell!"
    else:
      return "Paper covers rock, You Loose!"
  elif player == "Paper":
    if computer == "Rock":
      return "Paper covers Rock!, You win! How about that!"
    else:
      return "Scissors cuts rock, You lose!"
  elif player == "Scissors":
    if computer == "paper":
      return "Scissors cuts Paper!, You win! bloody hell!"
    else:
      return "Rock smashes Scissors, You Lose!, HA!HA!HA!"

while True:
  choices = get_choices() #This will access the dictionary values in the choices variable that is inside the get_Choices functiion.
  result = check_win(choices["player"], choices["computer"])
# Using brackets to access the value of the desired key. In the above case, the value of both the player and computer keys. 
  print(result)

  play_again = input("would you like to play again?").lower()

  if play_again != "yes":
    print("Bye!")
    break


  
