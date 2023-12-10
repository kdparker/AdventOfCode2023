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

# enclosed_grid = []
# for y, row in enumerate(grid):
#     row_output = ""
#     for x, tile in enumerate(row):
#         if (x, y) in visited_locations:
#             row_output += "L"
#         else:
#             row_output += "."
#     enclosed_grid.append(row_output)
# print(enclosed_grid)
# enclosed_count = 0

enclosed_locations = set()
outside_locations = set()
def check_if_enclosed(x, y):
    checked_locations = set()
    locations_to_check = [(x,y)]
    are_we_done = False
    squeeze_directions = {}
    while locations_to_check:
        location_to_check = locations_to_check.pop()

        loc_x = location_to_check[0]
        loc_y = location_to_check[1]
        if location_to_check in checked_locations:
            continue
        checked_locations.add(location_to_check)

        if (loc_y == 0 or loc_x == 0 or loc_y + 1 == len(grid) or loc_x + 1 == len(grid[0])):
            if location_to_check in visited_locations:
                continue
            outside_locations.add(location_to_check)
            for other_location_to_check in locations_to_check:
                outside_locations.add(other_location_to_check)
            for checked_location in checked_locations:
                outside_locations.add(checked_location)
            are_we_done = True
            break
        
        adjacent_locs = [
            (loc_x+1, loc_y),
            (loc_x-1, loc_y),
            (loc_x, loc_y-1),
            (loc_x, loc_y+1)
        ]
        tiles_to_investigate = []
        unsqueezable_tiles = [
            ("|"), #east
            ("|"), #west
            ("-"), #north
            ("-") #south
        ]
        if location_to_check in visited_locations: #we're squeezing
            dir = squeeze_directions[location_to_check]
            adjacent_loc = adjacent_locs[dir]
            if adjacent_loc not in checked_locations:
                if adjacent_loc in visited_locations:
                    tile_at_loc = grid[adjacent_loc[1]][adjacent_loc[0]]
                    if tile_at_loc in unsqueezable_tiles[dir]:
                        continue
                    tiles_to_investigate.append(adjacent_loc)
                    squeeze_directions[adjacent_loc] = dir
                else:
                    tiles_to_investigate.append(adjacent_loc)
        else:
            for dir, adjacent_loc in enumerate(adjacent_locs):
                if adjacent_loc not in checked_locations:
                    if adjacent_loc in visited_locations:
                        tile_at_loc = grid[adjacent_loc[1]][adjacent_loc[0]]
                        if tile_at_loc in unsqueezable_tiles[dir]:
                            continue
                        tiles_to_investigate.append(adjacent_loc)
                        squeeze_directions[adjacent_loc] = dir
                    else:
                        tiles_to_investigate.append(adjacent_loc)
        for tile_to_investigate in tiles_to_investigate:
            if tile_to_investigate in enclosed_locations:
                enclosed_locations.add(location_to_check)
                for other_location_to_check in locations_to_check:
                    enclosed_locations.add(other_location_to_check)
                for checked_location in checked_locations:
                    enclosed_locations.add(checked_location)
                for other_tile in tiles_to_investigate:
                    enclosed_locations.add(other_tile)
                are_we_done = True
                break
            if tile_to_investigate in outside_locations:
                outside_locations.add(location_to_check)
                for other_location_to_check in locations_to_check:
                    outside_locations.add(other_location_to_check)
                for checked_location in checked_locations:
                    outside_locations.add(checked_location)
                for other_tile in tiles_to_investigate:
                    outside_locations.add(other_tile)
                are_we_done = True
                break
        if are_we_done:
            break
        for tile_to_investigate in tiles_to_investigate:
            locations_to_check.append(tile_to_investigate)
    if not are_we_done:
        for checked_location in checked_locations:
            enclosed_locations.add(checked_location)



for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if (x, y) not in visited_locations:
            check_if_enclosed(x,y)

output = ""
for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if (x, y) in visited_locations:
            output += "*"
        elif (x,y) in enclosed_locations:
            output += "I"
        elif (x,y) in outside_locations:
            output += "O"
        else:
            output += "."
    output+= "\n"

print(output)

print(len(enclosed_locations.difference(visited_locations)))