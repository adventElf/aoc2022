from pprint import pprint
import re


def parse_input(input_file="../inputs/05_1.txt"):
    combined_inputs = open(input_file, "r").read().splitlines()
    cutpoint = combined_inputs.index("")
    cratemap = combined_inputs[:cutpoint]
    instructions = combined_inputs[cutpoint + 1 :]
    pprint(cratemap)

    stacks = [[], [], [], [], [], [], [], [], []]
    for row in cratemap[:8]:
        chunk = 3
        offset = 0
        for i in range(0, 9):
            stacks[i].append((row[offset + 1 : offset + chunk - 1]))
            offset += chunk
            offset += 1
    for i in range(0, len(stacks)):
        cutpoint = 0
        for element in stacks[i]:
            if element == " ":
                cutpoint += 1
        stacks[i] = stacks[i][cutpoint:]
    for stack in stacks:
        stack.reverse()

    return stacks, instructions


def execute_move(stacks, instruction):
    count, source, destination = re.findall(r"\b\d+\b", instruction)
    count = int(count)
    source = int(source) - 1
    destination = int(destination) - 1
    for i in range(0, count):
        crate = stacks[source][-1]
        stacks[destination].append(crate)
        del stacks[source][-1]
    return stacks


stacks, instructions = parse_input()

pprint(stacks)
for instruction in instructions:
    stacks = execute_move(stacks, instruction)

top_crates = ""
for stack in stacks:
    top_crates = top_crates + stack[-1]
print(top_crates)
