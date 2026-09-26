# Create 4 x 4 game board
board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


# Function to display the board
def print_board(board):
    print()

    for row in board:
        for number in row:
            if number == 0:
                print(".", end="\t")
            else:
                print(number, end="\t")

        print()

    print()


# Display the board
print_board(board)
