choice = ["rock", "paper", "scissors"]
print("Welcome to Rock Paper Scissors Game!")
player1_name = input("Hello player 1! Please enter your name: ").lower()
player2_name = input("Hello player 2! Please enter your name: ").lower()
while True:
    player1 = input( player1_name + " enter your choice: ").lower()
    if player1 not in choice:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue 
    player2 = input( player2_name + " enter your choice: ").lower()
    if player2 not in choice:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    if player1 == player2:
        print("It's a tie! Both players chose", player1)
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):   
        print(player1_name + " wins! {} beats {}".format(player1, player2))
    else:
        print(player2_name + " wins! {} beats {}".format(player2, player1))
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break        