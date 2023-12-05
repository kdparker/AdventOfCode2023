
with open("input.txt") as f:
    input = f.read()

parts_with_gear_adjacencies = {}

lines = input.splitlines()
for y, line in enumerate(lines):
    cur_number = ""
    gear_adjacencies = set()
    for x, char in enumerate(line):
        if char.isnumeric():
            cur_number += char
            check_range_x = range(max(0, x-1), min(x+1, len(line)-1) + 1)
            check_range_y = range(max(y-1, 0), min(y+1, len(lines)-1) + 1)
            for check_x in check_range_x:
                for check_y in check_range_y:
                    check_char = lines[check_y][check_x]
                    if check_char == "*":
                        gear_adjacencies.add((check_x, check_y))
        elif cur_number != "":
            finished_number = int(cur_number)
            cur_number = ""
            for gear in gear_adjacencies:
                current_parts_for_gear = parts_with_gear_adjacencies.get(gear, [])
                current_parts_for_gear.append(finished_number)
                parts_with_gear_adjacencies[gear] = current_parts_for_gear
            gear_adjacencies = set()
    if cur_number != "":
        finished_number = int(cur_number)
        cur_number = ""
        for gear in gear_adjacencies:
            current_parts_for_gear = parts_with_gear_adjacencies.get(gear, [])
            current_parts_for_gear.append(finished_number)
            parts_with_gear_adjacencies[gear] = current_parts_for_gear
        gear_adjacencies = set()

total_value = 0
for gear, numbers in parts_with_gear_adjacencies.items():
    if len(numbers) > 2:
        print("AHHHHH")
    if len(numbers) == 2:
        total_value += numbers[0] * numbers[1]
print(total_value)