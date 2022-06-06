import random

invalid_response = True

while invalid_response == True:
    
   
      human = input('Player 1(YOU) - Take a pick (R) for Rock, (P) for Paper, (S) for Scissors:\n')
      x = human.upper()
        
      if x == "R":
        print("You chose: Rock")
        invalid_response = False
        z = "Rock"
      elif x == "P":
        print("You chose: Paper")
        invalid_response = False
        z = "Paper"
      elif x == "S":
        print("You chose: Scissors")
        invalid_response = False
        z = "Scissors"
      else: print("Invalid choice please try again - Type R, P, or S")

computer_player = ["Paper", "Rock", "Scissors"]
y = random.choice(computer_player)

print("Player 2(COM) chose:")
print(y)

if z == y:
    print("It's a TIE, Play Again")
elif z == "Rock" and y == "Scissors":
    print("Player 1 wins!!!")
elif z == "Rock" and y == "Paper":
    print("Player 2 wins!!!")
elif z == "Scissors" and y == "Paper":
    print("Player 1 wins!!!")
elif z == "Scissors" and y == "Rock":
    print("Player 2 wins!!!")
elif z == "Paper" and y == "Rock":
    print("Player 1 wins!!!")
elif z == "Paper" and y == "Scissors":
    print("Player 2 wins!!!")








