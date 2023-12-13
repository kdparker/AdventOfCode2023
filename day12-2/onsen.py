import functools

with open("input.txt") as f:
    input = f.read()

@functools.cache
def number_of_possibilities_helper(parts, groupings, part_index, current_group_count, filled_groupings):
    if part_index == len(parts):
        is_valid = (
            (filled_groupings == len(groupings) and current_group_count == 0) or 
            (filled_groupings == len(groupings) - 1 and current_group_count == groupings[-1])
        )
        return 1 if is_valid else 0
    part = parts[part_index]
    if part == '#' and (filled_groupings >= len(groupings) or current_group_count > groupings[filled_groupings]):
        return 0
    if part == '#':
        return number_of_possibilities_helper(parts, groupings, part_index+1, current_group_count+1, filled_groupings)
    if part == '.' and current_group_count == 0:
        return number_of_possibilities_helper(parts, groupings, part_index+1, current_group_count, filled_groupings)
    if part == '.' and current_group_count != groupings[filled_groupings]:
        return 0
    if part == '.': # and current_group_count == groupings[filled_groupings]
        return number_of_possibilities_helper(parts, groupings, part_index+1, 0, filled_groupings+1)
    if filled_groupings < len(groupings) and current_group_count == groupings[filled_groupings]:
        return number_of_possibilities_helper(parts, groupings, part_index+1, 0 , filled_groupings+1)
    if filled_groupings < len(groupings) and current_group_count and current_group_count < groupings[filled_groupings]:
        return number_of_possibilities_helper(parts, groupings, part_index+1, current_group_count+1, filled_groupings)
    if filled_groupings < len(groupings) and current_group_count > groupings[filled_groupings]:
        return 0
    if filled_groupings == len(groupings) and current_group_count:
        return 0
    if filled_groupings == len(groupings): # and not current_group_count
        return number_of_possibilities_helper(parts, groupings, part_index+1, 0, filled_groupings)
    # part == '?', filled_groupings < len(groupings), current_group_count == 0
    return number_of_possibilities_helper(parts, groupings, part_index+1, 0, filled_groupings) + number_of_possibilities_helper(parts, groupings, part_index+1, 1, filled_groupings)

def get_number_of_possibilties_in_line(parts, groupings):
    if not '?' in parts:
        return 1
    
    possibilities = number_of_possibilities_helper(parts, groupings, 0, 0, 0)
    print(parts, groupings, possibilities)
    return possibilities

total_number_of_possibilities = 0
for x, line in enumerate(input.splitlines()):
    print("                #" + str(x))
    split_line = line.split()
    parts = split_line[0]
    groupings = tuple(map(int, split_line[1].strip().split(",")))
    folded_groupings = tuple(map(int, ",".join([split_line[1].strip()]*5).split(",")))
    folded_parts = "?".join([parts]*5)
    
    total_number_of_possibilities += get_number_of_possibilties_in_line(folded_parts, folded_groupings)
print(total_number_of_possibilities)