import os
from grid import create_grid, update_grid, print_grid
from save import  save_grid, load_last_grid

def game_manager():
    turn_pattern = None
    os.system('clear')
    choice = input("Enter 'n' for a new game or 'l' to load the last saved game: ").lower()
    if choice == 'l':
        grid, turn = load_last_grid()
        if grid is None:
            print("No saved game found. Starting a new game.")
            while True:
                try:
                    length = int(input("Enter the length of the grid (3-50): "))
                    if length < 3 or length > 50:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer between 1 and 50.")
            grid = create_grid(length)
            grid_pattern = create_grid(length)
            turn = 0
        else:
            length = len(grid)
            grid_pattern = [row[:] for row in grid]
    else:
        while True:
            try:
                length = int(input("Enter the length of the grid (3-50): "))
                if length < 3 or length > 50:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer between 1 and 50.")
        grid = create_grid(length)
        grid_pattern = create_grid(length)
        turn = 0

    print_grid(grid)
    while True:
        turn += 1
        if turn % 2 == 0:
            if grid_pattern == grid:
                if turn_pattern is None:
                    turn_pattern = turn
                print(f"It's a pattern since the turn: {turn_pattern}")
            grid_pattern = grid

        user_input = input("Press Enter to update the grid or 'q' to quit: ")
        if user_input.lower() == 'q':
            save_grid(grid, turn)
            break
        grid = update_grid(grid, length)
        os.system('clear')
        print(f"Turn: {turn}")
        print_grid(grid)
        save_grid(grid, turn)