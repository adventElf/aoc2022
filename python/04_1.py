pairs = open("../inputs/04_1.txt", "r").read().split("\n")


def extract_set_from_section_assignment(range_string):
    values = range_string.split("-")
    start = values[0]
    end = values[1]
    return set(range(int(start), int(end) + 1))


def process_pair(pair):
    range_pair = []
    for elf in pair.split(","):
        range_pair.append(extract_set_from_section_assignment(elf))
    return range_pair


def detect_full_overlap(set_pair):
    if set_pair[0].issubset(set_pair[1]) or set_pair[1].issubset(set_pair[0]):
        return True
    else:
        return False


overlaps = []
for pair in pairs:
    overlaps.append(detect_full_overlap(process_pair(pair)))
print(sum(overlaps))
