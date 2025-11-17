import random

choices = ["Rock", "Paper", "Scissors"]

rounds = int(input("How many rounds do you want to play? "))

player_score = 0
comp_score = 0

for _ in range(rounds):
    try:
         player = input("Enter Rock, Paper, or Scissors: ")
    except ValueErrors:
        print("Rock, Paper, or Scissors")
    comp = random.choice(choices)

    if player == comp:
        print("Tie")
    elif (player == "Rock" and comp == "Scissors") \
         or (player == "Paper" and comp == "Rock") \
         or (player == "Scissors" and comp == "Paper"):
        print("Player wins")
        player_score += 1
    else:
        print("Computer wins")
        comp_score += 1

    print("Player:", player)
    print("Computer:", comp)
    print()

print("Final Scores")
print("Player:", player_score)
print("Computer:", comp_score)