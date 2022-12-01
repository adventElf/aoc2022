input = open('../inputs/01_2.txt','r').read()

def build_elf_inventories(input):
    individuals = input.split('\n\n')
    elves = []
    for elf in individuals:
        this_elf = []
        for entry in elf.split('\n'):
            try:
                this_elf.append(int(entry))
            except:
                print(f'Cannot add {entry} as an integer.')
        elves.append(this_elf)
    return elves

elves = build_elf_inventories(input)

def sum_elf_calories(elf_inventory):
    calories = 0
    for entry in elf_inventory:
        calories += entry
    return calories

all_inventories = []
for elf in elves:
    all_inventories.append(sum_elf_calories(elf))
print(sum(sorted(all_inventories)[-3:]))