input = open('../inputs/01_1.txt','r').read()

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
        calories += int(entry)
    return calories

def find_extra_snacks(elves):
    extra_snacks_index = 0
    most_calories = 0

    for elf in elves:
        elf_calories = sum_elf_calories(elf)
        if elf_calories > most_calories:
            most_calories = elf_calories
            extra_snacks_index = elves.index(elf)
    
    print(f'Elf #{extra_snacks_index} is carrying {most_calories}.')
    return most_calories

find_extra_snacks(elves)