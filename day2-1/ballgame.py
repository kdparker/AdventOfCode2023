import re
game_regex = r"Game (\d+):(.*)"

with open("input.txt") as f:
    input = f.read()

RED = 12
GREEN = 13
BLUE = 14

total_value = 0
for line in input.splitlines():
    match = re.match(game_regex, line)
    game_no = int(match.group(1))
    games = match.group(2).split(";")
    possible = True
    for game in games:
        ball_sets = game.split(",")
        for balls in ball_sets:
            ball_sep = balls.strip().split(' ')
            ball_no = int(ball_sep[0])
            ball_color = ball_sep[1]
            if (ball_color == "red" and ball_no > RED) or (ball_color == "green" and ball_no > GREEN) or (ball_color == "blue" and ball_no > BLUE):
                possible = False
                break
        if not possible:
            break
    if possible:
        total_value += game_no
print(total_value)