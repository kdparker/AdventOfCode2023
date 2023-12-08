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

cur_nodes = []
for node_label in nodes.keys():
    if node_label[-1] == "A":
        cur_nodes.append(node_label)

def is_all_nodes_on_zs():
    z_count = 0
    for node_label in cur_nodes:
        if node_label[-1] == "Z":
            z_count += 1
    if z_count > 1:
        print(z_count, cur_nodes)
    return z_count == len(cur_nodes)

step_count = 0
while not is_all_nodes_on_zs():
    new_nodes = []
    next_step = steps[step_count % len(steps)]
    step_count += 1
    for node in cur_nodes:
        if next_step == "L":
            new_nodes.append(nodes[node].left)
        else:
            new_nodes.append(nodes[node].right)
    cur_nodes = new_nodes

print(step_count)