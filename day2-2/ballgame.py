import re
game_regex = r"Game (\d+):(.*)"

with open("input.txt") as f:
    input = f.read()

total_value = 0
for line in input.splitlines():
    match = re.match(game_regex, line)
    game_no = int(match.group(1))
    games = match.group(2).split(";")
    max_red = 0
    max_green = 0
    max_blue = 0
    for game in games:
        ball_sets = game.split(",")
        for balls in ball_sets:
            ball_sep = balls.strip().split(' ')
            ball_no = int(ball_sep[0])
            ball_color = ball_sep[1]
            if ball_color == "blue":
                max_blue = max(max_blue, ball_no)
            if ball_color == "green":
                max_green = max(max_green, ball_no)
            if ball_color == "red":
                max_red = max(max_red, ball_no)
    power = max_red * max_green * max_blue
    total_value += power
print(total_value)