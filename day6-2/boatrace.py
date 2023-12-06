with open("input.txt") as f:
    input = f.read()

lines = input.splitlines()
time = int("".join(lines[0].split(":")[1].strip().split()))
distance = int("".join(lines[1].split(":")[1].strip().split()))

def calculate_distance(total_time: int, time_spent_holding: int):
    return (total_time - time_spent_holding) * time_spent_holding

amount_of_wins = 0
for i in range(time+1):
    print(i/(time+1.0))
    if calculate_distance(time, i) > distance:
        amount_of_wins += 1


print(amount_of_wins)