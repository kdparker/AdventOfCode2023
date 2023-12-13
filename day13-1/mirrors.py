with open("input.txt") as f:
    input = f.read()

lines = input.splitlines()
grids = []
current_grid = []
for line in lines:
    if line == "":
        grids.append(current_grid)
        current_grid = []
    else:
        current_grid.append(line)
if current_grid:
    grids.append(current_grid)

def transpose_grid(grid):
    new_grid = []
    for i in range(len(grid[0])):
        line = ''.join([line[i] for line in grid])
        new_grid.append(line)
    return new_grid

def get_lines_above_reflection(grid):
    for i in range(1, len(grid)):
        above_index = i-1
        below_index = i
        is_reflected = True
        while above_index >= 0 and below_index < len(grid):
            if grid[above_index] != grid[below_index]:
                is_reflected = False
                break
            above_index -= 1
            below_index += 1
        if is_reflected:
            return i
    return 0

total_score = 0
for grid in grids:
    lines_above_reflection = get_lines_above_reflection(grid)
    if not lines_above_reflection:
        lines_above_reflection = get_lines_above_reflection(transpose_grid(grid))
    else:
        lines_above_reflection = 100 * lines_above_reflection
    total_score += lines_above_reflection
print(total_score)