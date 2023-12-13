with open("input.txt") as f:
    input = f.read()

def is_valid_groupings(parts, groupings):
    if '?' in parts:
        return False
    filled_groupings = 0
    current_group_count = 0
    for part in parts:
        if part == "#":
            current_group_count += 1
            continue
        if not current_group_count:
            continue
        if filled_groupings >= len(groupings):
            return False
        if groupings[filled_groupings] != current_group_count:
            return False
        current_group_count = 0
        filled_groupings += 1
    return (filled_groupings == len(groupings) and not current_group_count) or (filled_groupings == len(groupings) - 1 and current_group_count == groupings[filled_groupings])

def number_of_possibilities_helper(parts, groupings, damaged_to_place):
    if not damaged_to_place and '?' not in parts:
        is_valid = is_valid_groupings(parts, groupings)
        return 1 if is_valid else 0
    if damaged_to_place and '?' not in parts:
        return 0
    sum_of_possibilities = 0
    for i, part in enumerate(parts):
        if part == '?':
            if damaged_to_place > 0:
                sum_of_possibilities += number_of_possibilities_helper(parts[:i] + '#' + parts[i+1:], groupings, damaged_to_place-1)
            sum_of_possibilities += number_of_possibilities_helper(parts[:i] + '.' + parts[i+1:], groupings, damaged_to_place)
            break
    return sum_of_possibilities


def get_number_of_possibilties_in_line(parts, groupings):
    if not '?' in parts:
        return 1
    damaged_to_place = sum(groupings) - sum(map(lambda x: 1 if x == "#" else 0, parts))

    possibilities = number_of_possibilities_helper(parts, groupings, damaged_to_place)
    print(parts, groupings, possibilities)
    return possibilities

total_number_of_possibilities = 0
for line in input.splitlines():
    split_line = line.split()
    parts = split_line[0]
    groupings = list(map(int, split_line[1].split(',')))
    total_number_of_possibilities += get_number_of_possibilties_in_line(parts, groupings)
print(total_number_of_possibilities)