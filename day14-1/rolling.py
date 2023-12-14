with open("input.txt") as f:
    input = f.read()

grid = input.splitlines()
total = 0
for x in range(len(grid[0])):
    next_pos = 0
    for y in range(len(grid)):
        char = grid[y][x]
        if char == "O":
            total += len(grid) - next_pos
            next_pos = next_pos + 1
        elif char == "#":
            next_pos = y + 1

print(total)