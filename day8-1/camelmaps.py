from dataclasses import dataclass
import re

node_regex = r".*\((\w+), (\w+)\)"

@dataclass
class Node:
    left: str
    right: str

with open("input.txt") as f:
    input = f.read()

lines = input.splitlines()
steps = lines[0]

nodes = {}
for line in lines[2:]:
    label = line.split(" = ")[0]
    node_match = re.match(node_regex, line)
    nodes[label] = Node(node_match.group(1), node_match.group(2))

cur_node = "AAA"
step_count = 0
while cur_node != "ZZZ":
    next_step = steps[step_count % len(steps)]
    step_count += 1
    if next_step == "L":
        cur_node = nodes[cur_node].left
    else:
        cur_node = nodes[cur_node].right

print(step_count)