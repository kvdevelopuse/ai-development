# Colors
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


# function to display the board
def print_board(board_pos):
    display = []

    for value in board_pos:
        if value == "X":
            display.append(RED + "X" + RESET)
        elif value == "O":
            display.append(GREEN + "O" + RESET)
        else:
            display.append(str(value))

    print()
    for i in range(0, 9, 3):
        print(display[i], "|", display[i+1], "|", display[i+2])

        if i < 6:
            print("--|---|---")
    print()


def check_winner(board, player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
                board[position[1]] == player and
                board[position[2]] == player):
            return True

    return False


# Create game board
board = list(range(1, 10))

# X starts the game
player = "X"
moves_count = 0

# print the initial board
print_board(board)

while True:
    choice = input("Player " + player + ", enter your choice (1-9): ")

    # Check if input is a number
    if not choice.isdigit():
        print("Error: Please enter a number between 1 and 9.")
        continue

    choice = int(choice)

    # Check if number is between 1 and 9
    if choice < 1 or choice > 9:
        print("Error: Please enter a number between 1 and 9.")
        continue

    position = choice - 1
    print(position)

    # Check if position is already taken
    if board[position] == "X" or board[position] == "O":
        print("Position already taken. Please choose another position.")
        continue

    # Add X or O to the selected position
    board[position] = player
    moves_count += 1

    # Check if current player has won
    if check_winner(board, player):
        print("Player", player, "wins!")
        break

    # Check if the game is a draw
    if moves_count == 9:
        print("Game is a draw!")
        break

    # Switch player
    if player == "X":
        player = "O"
    else:
        player = "X"
