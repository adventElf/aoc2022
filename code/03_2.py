input = open("../inputs/03_1.txt", "r").read()
rucksacks = input.split("\n")
groups = []

for i in range(0, len(rucksacks), 3):
    x = i
    groups.append(rucksacks[x : x + 3])


lower = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,"
upper = lower.upper()
badge_types = (lower + upper[:-1]).split(",")


def prioritize(badge):
    return badge_types.index(badge) + 1


def detect_badge(group):
    for char in group[0]:
        if char in group[1] and char in group[2]:
            return char


priority_sum = 0

for group in groups:
    priority_sum += prioritize(detect_badge(group))

print(priority_sum)
