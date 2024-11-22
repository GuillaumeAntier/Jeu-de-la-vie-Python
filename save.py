import os

def save_grid(grid, turn):
    filename = 'last_save.txt'
    with open(filename, 'w') as f:
        f.write(f"{turn}\n")
        for row in grid:
            f.write(" ".join(str(cell) for cell in row) + '\n')

def load_last_grid():
    try:
        with open('last_save.txt', 'r') as f:
            turn = int(f.readline().strip())
            grid = [list(map(int, line.strip().split())) for line in f]
        return grid, turn
    except FileNotFoundError:
        return None, 0