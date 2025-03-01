def print_board(board):
    """Displays the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there's a winner on the board."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)

def play_game():
    """Main function to play the Tic-Tac-Toe game."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Player symbols
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Get the current player's move
        print(f"Player {players[current_player]}'s turn.")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter values between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("Cell already occupied! Choose a different cell.")
                continue

            # Make the move
            board[row][col] = players[current_player]
            print_board(board)

            # Check for a winner
            winner = check_winner(board)
            if winner:
                print(f"Player {winner} wins!")
                break

            # Check for a draw
            if is_full(board):
                print("It's a draw!")
                break

            # Switch players
            current_player = 1 - current_player

        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    play_game()
