# Create 4 x 4 game board
board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# to store random position of the empty cell to drop the new number
drop_position = 0

# Function to display the board


def print_board(board):
    print()
    print("+------+------+------+------+")

    for row in board:
        for number in row:
            if number == 0:
                print("|", "    ", end=" ")
            else:
                print("|", str(number).center(4), end=" ")

        print("|")
        print("+------+------+------+------+")

    print()


# Add starting numbers
board[0][0] = 2
board[1][1] = 2


def merge_row(row):
    numbers = []

    # remove zeros from the row
    for number in row:
        if number != 0:
            numbers.append(number)

    new_row = []
    i = 0

    # combine adjacent numbers if they are the same else keep the number as is
    while i < len(numbers):
        if i + 1 < len(numbers) and numbers[i] == numbers[i + 1]:
            new_row.append(numbers[i] * 2)
            i += 2
        else:
            new_row.append(numbers[i])
            i += 1

    # check if the new row has less than 4 elements and add zeros to the end of the row
    while len(new_row) < 4:
        new_row.append(0)

    return new_row


def move_left(board):
    new_board = []

    for row in board:
        new_row = merge_row(row)
        new_board.append(new_row)

    return new_board


def move_right(board):
    new_board = []

    for row in board:
        reverse_row = row[::-1]
        new_row = merge_row(reverse_row)
        new_row = new_row[::-1]
        new_board.append(new_row)

    return new_board


def move_up(board):
    new_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    for column in range(4):
        column_values = []

        # Get values from the column
        for row in range(4):
            column_values.append(board[row][column])

        # Merge the column
        new_column = merge_row(column_values)

        # Put values back into the new board
        for row in range(4):
            new_board[row][column] = new_column[row]

    return new_board


def move_down(board):
    new_board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    for column in range(4):
        column_values = []

        # Get values from the column
        for row in range(4):
            column_values.append(board[row][column])

        # Reverse the column
        column_values = column_values[::-1]

        # Merge the column
        new_column = merge_row(column_values)

        # Reverse it back
        new_column = new_column[::-1]

        # Put values back into the new board
        for row in range(4):
            new_board[row][column] = new_column[row]

    return new_board

# Function to add a new number in empty cell of the board


def add_new_number(board):
    global drop_position

    empty_positions = []

    # Find all empty positions
    for row in range(4):
        for column in range(4):
            if board[row][column] == 0:
                empty_positions.append([row, column])

    # Add 2 to a changing empty position
    if len(empty_positions) > 0:
        drop_position = (drop_position + 3) % len(empty_positions)

        row = empty_positions[drop_position][0]
        column = empty_positions[drop_position][1]

        board[row][column] = 2


def check_win(board):
    for row in board:
        for number in row:
            if number == 2048:
                return True

    return False


def check_game_over(board):
    # Check if there are empty cells
    for row in board:
        for number in row:
            if number == 0:
                return False

    # Check if horizontal numbers can merge
    for row in range(4):
        for column in range(3):
            if board[row][column] == board[row][column + 1]:
                return False

    # Check if vertical numbers can merge
    for row in range(3):
        for column in range(4):
            if board[row][column] == board[row + 1][column]:
                return False

    return True


print("2048 Game")
print("U = Up | D = Down | L = Left | R = Right | Q = Quit")
old_board = []

while True:
    print_board(board)

    choice = input("Enter move (U=Up/D=Down/L=Left/R=Right) or Q to quit: ")
    choice = choice.lower()

    if choice == "q":
        print("Game ended.")
        break

    if choice != "u" and choice != "d" and choice != "l" and choice != "r":
        print("Invalid choice. Please enter U, D, L, R or Q.")
        continue

    if choice == "l":
        board = move_left(board)

    elif choice == "r":
        board = move_right(board)

    elif choice == "u":
        board = move_up(board)

    elif choice == "d":
        board = move_down(board)

    # Add a new number only if the board changed
    if board != old_board:
        add_new_number(board)
    else:
        print("No tiles moved. Try another direction.")

    # Check if player reached 2048
    if check_win(board):
        print_board(board)
        print("Congratulations! You reached 2048!")
        break

    # Check if there are no more possible moves
    if check_game_over(board):
        print_board(board)
        print("Game Over!")
        break
