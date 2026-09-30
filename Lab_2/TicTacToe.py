board = list("123456789")
player = "X"
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

while True:
    print("\n" + "\n".join(" ".join(board[i:i+3]) for i in (0, 3, 6)))

    while True:
        choice = input(f"{player}, enter position (1-9): ")
        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Enter a number from 1 to 9.")
        elif board[int(choice) - 1] in "XO":
            print("Taken, try again.")
        else:
            pos = int(choice) - 1
            break

    board[pos] = player

    if any(board[a] == board[b] == board[c] for a, b, c in wins):
        print("\n" + "\n".join(" ".join(board[i:i+3]) for i in (0, 3, 6)))
        print(player, "wins!")
        break
    if all(s in "XO" for s in board):
        print("Draw")
        break

    player = "O" if player == "X" else "X"
