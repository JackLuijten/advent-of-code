import os

with open('data/day18.csv') as f:
    input = [[int(i) for i in j.split(',')] for j in f.read().split('\n')]

qubes = set()
empty = set()
visible_sides = 0

for x in range(26):
    for y in range(26):
        for z in range(26):
            empty.add((x,y,z))

for i in input:
    x, y, z = i
    qubes.add((x, y, z))

for p in qubes:
    x, y, z = p
    qube_sides = 6
    sides = set()
    for point in [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]:
        sides.add(point)
        # empty.add(point)
    visible_sides += qube_sides - len(sides.intersection(qubes))
empty = empty.difference(qubes)
print(visible_sides)

keepgoing = True
turn = 0
while keepgoing:
    remove = set()
    for e in empty:
        x, y, z = e
        for point in [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]:
            if point in empty or point in qubes:
                continue
            else:
                remove.add(e)
                break
    empty = empty.difference(remove)
    if len(remove) == 0:
        keepgoing = False

for e in empty:
    x, y, z = e
    for point in [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]:
        if point in qubes:
            visible_sides -= 1

print(visible_sides)

# Code block to delete hovering qubes. It removes to many edges, so commented out
# for q in qubes:
#     x, y, z = q
#     empty_sides = 0
#     for point in [(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)]:
#         if point in empty:
#             empty_sides += 1
#     if empty_sides == 6:
#         print(q, empty_sides)
#         visible_sides -= 6
# print(visible_sides)

# TOO HIGH 3998
# TOO HIGH 3986
# CORRECT 2468
