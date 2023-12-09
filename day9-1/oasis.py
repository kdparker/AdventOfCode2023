
with open("input.txt") as f:
    input = f.read()

def all_zeroes(l):
    for v in l:
        if v != 0:
            return False
    return True

histories = list(map(lambda x: list(map(int, x.split())), input.splitlines()))
full_diff_histories = []
for history in histories:
    sequences = [history]
    while not all_zeroes(sequences[-1]):
        new_sequence = []
        last_sequence = sequences[-1]
        last_val = last_sequence[0]
        for val in last_sequence[1:]:
            new_sequence.append(val-last_val)
            last_val = val
        sequences.append(new_sequence)
    full_diff_histories.append(sequences)

results = []
for full_diff_history in full_diff_histories:
    to_add = 0
    for sequence in full_diff_history[::-1]:
        to_add += sequence[-1]
    results.append(to_add)

print(sum(results))