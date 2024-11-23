import random
import os

def initialize_board():
    """Initialize a 4x4 board with two random tiles."""
    board = [[0] * 4 for _ in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    return board

def add_random_tile(board):
    """Add a random 2 or 4 to an empty spot on the board."""
    empty_tiles = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        board[r][c] = 2 if random.random() < 0.9 else 4

def print_board(board):
    """Print the game board in the console."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for row in board:
        print("+----" * 4 + "+")
        print("".join(f"| {tile or ' ':<4}" for tile in row) + "|")
    print("+----" * 4 + "+")

def compress(board):
    """Slide all tiles to the left."""
    new_board = []
    for row in board:
        new_row = [tile for tile in row if tile != 0]
        new_row += [0] * (4 - len(new_row))
        new_board.append(new_row)
    return new_board

def merge(board):
    """Merge adjacent tiles of the same value."""
    for row in board:
        for i in range(3):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
    return board

def reverse(board):
    """Reverse the rows of the board."""
    return [row[::-1] for row in board]

def transpose(board):
    """Transpose the board (rows become columns and vice versa)."""
    return [list(row) for row in zip(*board)]

def move_left(board):
    """Perform a left move (slide + merge + slide)."""
    board = compress(board)
    board = merge(board)
    return compress(board)

def move_right(board):
    """Perform a right move."""
    board = reverse(board)
    board = move_left(board)
    return reverse(board)

def move_up(board):
    """Perform an up move."""
    board = transpose(board)
    board = move_left(board)
    return transpose(board)

def move_down(board):
    """Perform a down move."""
    board = transpose(board)
    board = move_right(board)
    return transpose(board)

def check_game_over(board):
    """Check if there are no valid moves left."""
    for move in [move_left, move_right, move_up, move_down]:
        if move([row[:] for row in board]) != board:
            return False
    return True

def main():
    """Main game loop."""
    board = initialize_board()
    while True:
        print_board(board)
        if any(2048 in row for row in board):
            print("Congratulations! You reached 2048!")
            break
        if check_game_over(board):
            print("Game Over! No more moves available.")
            break
        move = input("Enter move (W/A/S/D): ").lower()
        if move == "w":
            new_board = move_up(board)
        elif move == "a":
            new_board = move_left(board)
        elif move == "s":
            new_board = move_down(board)
        elif move == "d":
            new_board = move_right(board)
        else:
            print("Invalid move! Please use W/A/S/D.")
            continue
        if new_board != board:
            board = new_board
            add_random_tile(board)
        else:
            print("Invalid move! Try a different direction.")

if __name__ == "__main__":
    main()