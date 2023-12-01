
with open("input.txt") as f:
    input = f.read()

total_value = 0
for line in input.splitlines():
    first_digit = None
    last_digit = None
    for c in line:
        if c.isnumeric():
            first_digit = int(c)
            break
    for c in line[::-1]:
        if c.isnumeric():
            last_digit = int(c)
            break
    line_value = (first_digit*10) + last_digit
    total_value += line_value
    
print(total_value)