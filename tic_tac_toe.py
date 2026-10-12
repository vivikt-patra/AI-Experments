#Function to display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

#Function to check the winner
def check_winner(board):
    #check rows
    for row in board:
        if row[0]== row[1] == row[2] != " ":
            return True

    #check columns
    for col in range(3):
        if board[0][col]==board[1][col]== board[2][col] != " ":
        return True
    
    #check diagonals
    if board[0][0]== board[1][1]== board[2][2] !=" ":
        return True

    if board[0][2]== board[1][1]==board[2][0] !=" ":
        return True
    
    return False

#Main Program
board[[" " for_ in range(3)]for _ in range(3)]

player = "X"

for turn in range(9)
    print("\n Current Board: ")
    print_board(board)

    print(f"Player {player}'s Turn")
   
    row= int(input("Enter row(0-2):"))
    col= int(input("Enter Column(0-2):"))

    if board[row][col]==" ":
        board[row][col] = player