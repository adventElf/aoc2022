from anytree import Node
from pprint import pprint
from anytree.exporter import JsonExporter
import re, json

cutoff = 100_000
input = "../inputs/07.txt"

cwd = None
with open(input, "r") as fp:
    for line in fp:
        its_a_change_directory = re.search(r"\$ cd (.+)", line)
        its_a_file = re.search(r"(\d+) (.+)", line)
        if its_a_change_directory:
            name = its_a_change_directory.group(1)
            cwd = Node(name, parent=cwd) if name != ".." else cwd.parent
        elif its_a_file:
            Node(its_a_file.group(2), size=its_a_file.group(1), parent=cwd)

sizes = {}
for leaf in cwd.root.leaves:
    size = int(leaf.size)
    for a in leaf.ancestors:
        path = "/".join([x.name for x in a.path])
        sizes[path] = size if path not in sizes else sizes[path] + size

total_space = 70_000_000
space_needed = 30_000_000
disk_used = total_space - sizes["/"]
disk_space_to_clean = space_needed - disk_used

a = sum([x for x in sizes.values() if x <= cutoff])
b = min([x for x in sizes.values() if x >= disk_space_to_clean])

print(f"Total size of all directories under size {cutoff}: \n\t{a}")
print(
    f"Total size of the smallest directory big enough to free up {space_needed} of space: \n\t{b}"
)
