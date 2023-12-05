
with open("input.txt") as f:
    input = f.read()

total_value = 0
for line in input.splitlines():
    card = line.split(':')[1].strip()
    winning_numbers_line = card.split('|')[0].strip()
    numbers_line = card.split('|')[1].strip()
    winning_numbers = set()
    card_value = 0
    for winning_number in winning_numbers_line.split():
        winning_numbers.add(int(winning_number))
    for number in numbers_line.split():
        if int(number) in winning_numbers:
            card_value = 1 if not card_value else card_value * 2
    total_value += card_value
print(total_value)