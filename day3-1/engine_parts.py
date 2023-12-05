
with open("input.txt") as f:
    input = f.read()

total_value = 0

lines = input.splitlines()
for y, line in enumerate(lines):
    cur_number = ""
    is_adjacent = False
    for x, char in enumerate(line):
        if char.isnumeric():
            cur_number += char
            if not is_adjacent:
                check_range_x = range(max(0, x-1), min(x+1, len(line)-1) + 1)
                check_range_y = range(max(y-1, 0), min(y+1, len(lines)-1) + 1)
                print(x, y, list(check_range_x), list(check_range_y))
                for check_x in check_range_x:
                    for check_y in check_range_y:
                        check_char = lines[check_y][check_x]
                        if not check_char.isnumeric() and check_char != ".":
                            is_adjacent = True
                            break
                    if is_adjacent:
                        break
        elif cur_number != "":
            finished_number = int(cur_number)
            cur_number = ""
            if is_adjacent:
                total_value += finished_number
            is_adjacent = False
    if cur_number != "":
        finished_number = int(cur_number)
        cur_number = ""
        if is_adjacent:
            total_value += finished_number
print(total_value)