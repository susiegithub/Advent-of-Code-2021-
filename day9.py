import numpy as np
with open("day9.txt") as file:
    data = file.read().split("\n")
data = [list(map(int, [c for c in line])) for line in data]
data = np.array(data)
padArr = np.pad(data, 1, "constant", constant_values=10)
counter = 0 
basins = []
basins2 = []
def find(i,h):
    global counter, basins, above, below, right, left
    val = padArr[i+1][h+1]
    above = padArr[i][h+1]
    below = padArr[i+2][h+1]
    right = padArr[i+1][h+2]
    left = padArr[i+1][h]
    if val < above and val < below and val < left and val < right:
        basins.append([i+1,h+1])
        counter +=1
        ifNot9(i+1,h+1) 
        
def ifNot9(i,h):
    global basins
    above = padArr[i-1][h]
    below = padArr[i+1][h]
    right = padArr[i][h+1]
    left = padArr[i][h-1]
    if above < 9:
        if [i-1, h] not in basins:
            basins.append([i-1,h])
            ifNot9(i-1, h)
    if below < 9:
        if [i+1, h] not in basins:
            basins.append([i+1, h])
            ifNot9(i+1, h)
    if right < 9:
        if [i, h+1] not in basins:
            basins.append([i, h+1])
            ifNot9(i, h+1)
    if left < 9:
        if [i, h-1] not in basins:
            basins.append([i, h-1])
            ifNot9(i, h-1)


for i in range(len(data)):
    for h in range(len(data[i])):
        find(i,h)
        basinsize = len(basins)
        basins = []
        basins2.append(basinsize)
basins2 = sorted([x for x in basins2 if x!=0])
length = len(basins2)
print(basins2[length-1]*basins2[length-2]*basins2[length-3])