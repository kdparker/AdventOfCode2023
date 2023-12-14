with open("input.txt") as f:
    input = f.read()

grid = input.splitlines()

height = len(grid)
width = len(grid[0])

def grid_for_positions(grid, positions):
    new_grid = []
    for y, row in enumerate(grid):
        new_row = ""
        for x, tile in enumerate(row):
            new_row += "." if tile != "#" and (x, y) not in positions else ("O" if (x,y) in positions else "#")
        new_grid.append(new_row)
    return new_grid

def tilt_north(grid):
    positions = set()
    for x in range(width):
        next_pos = 0
        for y in range(height):
            char = grid[y][x]
            if char == "O":
                positions.add((x,next_pos))
                next_pos = next_pos + 1
            elif char == "#":
                next_pos = y + 1
    return grid_for_positions(grid, positions)

def tilt_south(grid):
    positions = set()
    for x in range(width):
        next_pos = height-1
        for y in range(height-1, -1, -1):
            char = grid[y][x]
            if char == "O":
                positions.add((x,next_pos))
                next_pos = next_pos - 1
            elif char == "#":
                next_pos = y - 1
    return grid_for_positions(grid, positions)

def tilt_west(grid):
    positions = set()
    for y in range(height):
        next_pos = 0
        for x in range(width):
            char = grid[y][x]
            if char == "O":
                positions.add((next_pos, y))
                next_pos = next_pos + 1
            elif char == "#":
                next_pos = x + 1
    return grid_for_positions(grid, positions)

def tilt_east(grid):
    positions = set()
    for y in range(height):
        next_pos = width-1
        for x in range(width-1, -1, -1):
            char = grid[y][x]
            if char == "O":
                positions.add((next_pos, y))
                next_pos = next_pos - 1
            elif char == "#":
                next_pos = x - 1
    return grid_for_positions(grid, positions)

def spin(grid):
    return tilt_east(tilt_south(tilt_west(tilt_north(grid))))

def calculate_value(grid):
    total = 0
    for y, row in enumerate(grid):
        for char in row:
            if char == "O":
                total += height-y
    return total

max = 1000
values = []
for i in range(max):
    print(str(i) + ", " + str(calculate_value(grid)))
    grid = spin(grid)
