
with open("input.txt") as f:
    input = f.read()

scratch_card_values = {}
lines = input.splitlines()
for i in range(len(lines)-1, -1, -1):
    line = lines[i]
    card_no = i+1
    card = line.split(':')[1].strip()
    winning_numbers_line = card.split('|')[0].strip()
    numbers_line = card.split('|')[1].strip()
    winning_numbers = set()
    match_count = 0
    for winning_number in winning_numbers_line.split():
        winning_numbers.add(int(winning_number))
    for number in numbers_line.split():
        if int(number) in winning_numbers:
            match_count += 1
    line_value = 1
    print(card_no, list(range(card_no+1, card_no+match_count+1)))
    for additional_card in range(card_no+1, card_no+match_count+1):
        line_value += scratch_card_values[additional_card]
    scratch_card_values[card_no] = line_value


total_value = 0
for scratch_card_value in scratch_card_values.values():
    total_value += scratch_card_value
print(total_value)