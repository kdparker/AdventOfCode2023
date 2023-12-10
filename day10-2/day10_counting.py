import sys
sys.setrecursionlimit(200000)
with open("input.txt") as f:
    input = f.read()

grid = input.splitlines()
s_location = None
for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if tile == "S":
            s_location = (x, y)
            break
    if s_location is not None:
        break

max_distance = 0
visited_locations = set()

def get_max_distance_from_animal(cur_location, cur_distance):
    global max_distance
    if cur_location in visited_locations:
        return
    if cur_distance > max_distance:
        max_distance = cur_distance
    visited_locations.add(cur_location)
    connected_points = []
    x = cur_location[0]
    y = cur_location[1]
    tile = grid[y][x]
    # Check north
    if tile in ("|", "L", "J", "S") and y > 0 and grid[y - 1][x] in ("|", "7", "F") and (x, y - 1) not in visited_locations:
        connected_points.append((x, y - 1))
    # Check south
    if tile in ("|", "7", "F", "S") and y + 1 < len(grid) and grid[y + 1][x] in ("|", "L", "J") and (x, y + 1) not in visited_locations:
        connected_points.append((x, y + 1))
    # Check West
    if tile in ("-", "J", "7", "S") and x > 0 and grid[y][x - 1] in ("-", "L", "F") and (x - 1, y) not in visited_locations:
        connected_points.append((x - 1, y))
    # Check East
    if tile in ("-", "L", "F", "S")  and x + 1 < len(grid[0]) and grid[y][x + 1] in ("-", "J", "7") and (x + 1, y) not in visited_locations:
        connected_points.append((x + 1, y))
    for connected_point in connected_points:
        get_max_distance_from_animal(connected_point, cur_distance+1)


get_max_distance_from_animal(s_location, 0)

enclosed_locations = set()
for y, row in enumerate(grid):
    north_facing_tiles_seen = 0
    for x, tile in enumerate(row):
        if (x,y) in visited_locations and grid[y][x] in ("|", "L", "J"): #hardcoded s
            north_facing_tiles_seen += 1
        elif (x,y) not in visited_locations:
            if north_facing_tiles_seen % 2 == 1:
                enclosed_locations.add((x,y))

output = ""
for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if (x, y) in visited_locations:
            output += grid[y][x]
        else:
            output += "."
    output+= "\n"
print(len(enclosed_locations))