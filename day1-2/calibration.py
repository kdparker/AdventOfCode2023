
with open("input.txt") as f:
    input = f.read()

possible_digits = [
    ('one', 1),
    ('two', 2),
    ('three', 3),
    ('four', 4),
    ('five', 5),
    ('six', 6),
    ('seven', 7),
    ('eight', 8),
    ('nine', 9),
    ('zero', 0)
]

def get_first_digit_in_line(line: str, reversed: bool) -> int:
    last_five_chars = ""
    for c in line:
        if c.isnumeric():
            return int(c)
        last_five_chars = last_five_chars + c if not reversed else c + last_five_chars
        last_five_chars = last_five_chars[-5:] if not reversed else last_five_chars[:5]
        for possible_digit, value in possible_digits:
            if possible_digit in last_five_chars:
                return value


total_value = 0
for line in input.splitlines():
    first_digit = None
    last_digit = None
    first_digit = get_first_digit_in_line(line, False)
    last_digit = get_first_digit_in_line(line[::-1], True)
    line_value = (first_digit*10) + last_digit
    total_value += line_value
    
print(total_value)