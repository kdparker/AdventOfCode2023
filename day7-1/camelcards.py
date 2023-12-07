import functools

with open("input.txt") as f:
    input = f.read()

lines = input.splitlines()
hands = []
sorted_hands = []

card_values = 'AKQJT98765432'

def compare_cards(a: str, b:str):
    if a == b:
        return 0
    a_pos = card_values.find(a)
    b_pos = card_values.find(b)
    return 1 if a_pos < b_pos else -1

def higher_value_card_hands(a:str, b:str):
    for a_char, b_char in zip(a, b):
        if compare_cards(a_char, b_char) != 0:
            return compare_cards(a_char, b_char)
    return 0

def get_card_counts(hand:str):
    counts = {}
    for card in hand:
        cur_count = counts.get(card, 0)
        cur_count += 1
        counts[card] = cur_count
    return counts

def is_five_of_kind(card_counts):
    return 5 in card_counts.values()

def is_four_of_kind(card_counts):
    return 4 in card_counts.values()

def is_full_house(card_counts):
    return 3 in card_counts.values() and 2 in card_counts.values()

def is_three_of_kind(card_counts):
    return 3 in card_counts.values() and 2 not in card_counts.values()

def is_two_pair(card_counts):
    found_pairs = 0
    for count in card_counts.values():
        if count == 2:
            found_pairs += 1
    return found_pairs == 2

def is_pair(card_counts):
    found_pairs = 0
    for count in card_counts.values():
        if count == 2:
            found_pairs += 1
    return found_pairs == 1 and 3 not in card_counts.values()

def get_hand_value(hand):
    card_counts = get_card_counts(hand)
    if is_five_of_kind(card_counts):
        return 6
    if is_four_of_kind(card_counts):
        return 5
    if is_full_house(card_counts):
        return 4
    if is_three_of_kind(card_counts):
        return 3
    if is_two_pair(card_counts):
        return 2
    if is_pair(card_counts):
        return 1
    return 0

def compare_hands(a:str, b:str):
    a_hand_value = get_hand_value(a)
    b_hand_value = get_hand_value(b)
    if a_hand_value > b_hand_value:
        return 1
    elif b_hand_value > a_hand_value:
        return -1
    return higher_value_card_hands(a, b)

def parse_hand(line):
    split_line = line.split()
    return (split_line[0], int(split_line[1]))

def compare_full_hands(a, b):
    return compare_hands(a[0], b[0])

full_hands = list(map(parse_hand, lines))   
full_hands.sort(key=functools.cmp_to_key(compare_full_hands))


total_value = 0
for i, hand in enumerate(full_hands):
    total_value += hand[1] * (i+1)

print(total_value)
