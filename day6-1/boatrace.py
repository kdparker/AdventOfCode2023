with open("input.txt") as f:
    input = f.read()

lines = input.splitlines()
times = list(map(int, lines[0].split(":")[1].strip().split()))
distances = list(map(int, lines[1].split(":")[1].strip().split()))

def calculate_distance(total_time: int, time_spent_holding: int):
    return (total_time - time_spent_holding) * time_spent_holding

races = zip(times, distances)
total_value = 1
for time, distance in races:
    amount_of_wins = 0
    for i in range(time+1):
        if calculate_distance(time, i) > distance:
            amount_of_wins += 1
    total_value *= amount_of_wins

print(total_value)