with open("input.txt") as f:
    input = f.read()

grid = input.splitlines()
empty_rows = []
for y, row in enumerate(grid):
    if row == '.' * len(row):
        empty_rows.append(y)
empty_columns = []
for x in range(len(grid[0])):
    is_empty = True
    for y in range(len(grid)):
        if grid[y][x] != ".":
            is_empty = False
            break
    if is_empty:
        empty_columns.append(x)

for i, empty_row_index in enumerate(empty_rows):
    grid = grid[:empty_row_index+i+1] + [grid[empty_row_index+i]] + grid[empty_row_index+i+1:]

for i, empty_column_index in enumerate(empty_columns):
    for y in range(len(grid)):
        grid[y] = grid[y][:empty_column_index+i+1] + '.' + grid[y][empty_column_index+i+1:]

galaxy_locations = []
for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if grid[y][x] == "#":
            galaxy_locations.append((x,y))

sum_of_diff = 0
for i, galaxy_location in enumerate(galaxy_locations):
    for other_location in galaxy_locations[i+1:]:
        sum_of_diff += abs(galaxy_location[0] - other_location[0]) + abs(galaxy_location[1] - other_location[1])

print(sum_of_diff)