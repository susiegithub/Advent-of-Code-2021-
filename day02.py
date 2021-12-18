horizontal = 0 
depth = 0
aim = 0 
def distance(distance):
    split = x.split()
    if split[0] == "forward":
        global horizontal, depth, aim
        depth += aim*int(split[1])
        horizontal += int(split[1])
    elif split[0] == "down":
        aim += int(split[1])
    elif split[0] == "up":
        aim -= int(split[1])

file = open("day2.txt", "r")
for x in file:
    distance(x)

print(horizontal * depth)
