winning_combinations = [
    [1,2,3],[4,5,6],[7,8,9], #rows_wise
    [1,4,7],[2,5,8],[3,6,9],#column_wise
    [1,5,9],[3,5,7]#diagonal_wise 
]
move_list = []
player_1 = []
player_2 = []
def check_winner(winner):
    for arr in winning_combinations:
        for arr2 in arr:
            if arr2 not in winner:
                break
        else:
            return True
    return False
for turn in range (9):
    while (True):
        move = int(input("Player 1 Enter Your Move 1 to 9: "))
        if move<1 or move>9:
            print("Invalid Input!!")
            continue
        if move in player_1 + player_2:
            print("Mistake! Try another Input")
            continue
        player_1.append(move)  
        print(player_1)
        break
    if check_winner(player_1):
        print("Player 1 wins!!")
        break
    while (True):
        move = int(input("Player 2 Enter Your Move 1 to 9: "))
        if move<1 or move>9:
            print("Invalid Input!!")
            continue
        if move in player_1 + player_2:
            print("Mistake! Try another Input")
            continue
        player_2.append(move)  
        print(player_2)
        break
    if check_winner(player_2):
        print("Player 2 wins!!")
        break
else: 
    print("Draw")