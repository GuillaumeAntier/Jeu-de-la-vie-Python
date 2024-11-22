import random
import os
length = int(input("Enter the length of the grid: "))

def create_grid():
    
    grid = ([[random.choice([0, 1]) for _ in range(length)] for _ in range(length)])

    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join('⬜' if cell == 1 else '⬛' for cell in row))

def update_grid(grid):
    new_grid= ([[0] * length for _ in range(length)])
    for i in range(length):
        for j in range(length):
            alive_neighbors = count_alive_neighbour(grid,i,j)
            if grid[i][j] == 1:
                new_grid[i][j] = 1 if alive_neighbors in [2, 3] else 0
            else:
                new_grid[i][j] = 1 if alive_neighbors == 3 else 0
    return new_grid

def count_alive_neighbour(grid,x,y):
    direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    count = 0
    for direction_x, direction_y in direction :
        new_x, new_y = x + direction_x, y + direction_y 
        if 0 <= new_x < length and 0 <= new_y < length :
            count += grid[new_x][new_y]
    return count

def save_grid(grid, turn):
    filename = f'grid_state_turn_{turn}.txt'
    with open(filename, 'w') as f:
        for row in grid:
            f.write(" ".join(str(cell) for cell in row) + '\n')
    with open('last_save.txt', 'w') as f:
        f.write(filename)

def load_last_grid():
    try:
        with open('last_save.txt', 'r') as f:
            filename = f.read().strip()
        with open(filename, 'r') as f:
            grid = [list(map(int, line.strip().split())) for line in f]
        turn = int(filename.split('_')[-1].split('.')[0])
        return grid, turn
    except FileNotFoundError:
        return None, 0
    
def main():
    choice = input("Enter 'n' for a new game or 'l' to load the last saved game: ").lower()
    if choice == 'l':
        grid, turn = load_last_grid()
        if grid is None:
            print("No saved game found. Starting a new game.")
            grid = create_grid()
            turn = 0
    else:
        grid = create_grid()
        turn = 0

    print_grid(grid)
    while True:
        turn += 1
        user_input = input("Press Enter to update the grid or 'q' to quit: ")
        if user_input.lower() == 'q':
            save_grid(grid, turn)
            break
        grid = update_grid(grid)
        os.system('clear')
        print(f"Turn: {turn}")
        print_grid(grid)
        save_grid(grid, turn)

if __name__ == "__main__":
    main()

