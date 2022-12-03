input = open("../inputs/03_1.txt", "r").read()
rucksacks = input.split("\n")
compartments = []
for rucksack in rucksacks:
    l = len(rucksack)
    s = int(l / 2)
    compartments.append([rucksack[0:s], rucksack[s:l]])

lower = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,"
upper = lower.upper()
item_types = (lower + upper[:-1]).split(",")


def prioritize(item_type):
    return item_types.index(item_type) + 1


def check_compartments(rucksack):
    for char in rucksack[0]:
        if char in rucksack[1]:
            return char


priority_sum = 0
for rucksack in compartments:
    priority_sum += prioritize(check_compartments(rucksack))

print(priority_sum)
