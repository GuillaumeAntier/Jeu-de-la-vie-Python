import random


def create_grid(length):
    
    grid = ([[random.choice([0, 1]) for _ in range(length)] for _ in range(length)])

    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join('⬜' if cell == 1 else '⬛' for cell in row))

def update_grid(grid,length):
    new_grid= ([[0] * length for _ in range(length)])
    for i in range(length):
        for j in range(length):
            alive_neighbors = count_alive_neighbour(grid,i,j,length)
            if grid[i][j] == 1:
                new_grid[i][j] = 1 if alive_neighbors in [2, 3] else 0
            else:
                new_grid[i][j] = 1 if alive_neighbors == 3 else 0
    return new_grid

def count_alive_neighbour(grid,x,y,length):
    direction = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    count = 0
    for direction_x, direction_y in direction :
        new_x, new_y = x + direction_x, y + direction_y 
        if 0 <= new_x < length and 0 <= new_y < length :
            count += grid[new_x][new_y]
    return count
