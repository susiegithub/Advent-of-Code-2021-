import numpy as np
with open("day11.txt") as file:
    data = file.read().split("\n")
data2 = []
rowLen = len(data[0])
numRow = len(data)
for x in data:
    data2.append([x[i:i+1] for i in range(0, len(x), 1)])
data = []
for x in data2:
    data.append(list(map(int, x))) # this is all to split up the elements and make them int
    
data = np.array(data)
data = data.reshape(numRow, rowLen)
data2 = data
data = np.pad(data, 1, "constant", constant_values=-1000) #after this data is in suitable format 

flashes = []
flashCount = 0
def set0(i,j):
    global flashes, data
    for x in flashes:
        data[x[0]][x[1]] = 0
        
def add1(x):
    global data
    for i in range(len(data)):
        data[i] = [x+1 for x in data[i]]
        
def flash(i,j):
    global data, flashes, flashCount
    val = data[i][j]
    if val > 9 and [i,j] not in flashes:
        flashes.append([i,j])
        flashCount += 1
        flash2(i,j)
                
def flash2(i,j):
    global data, flashes, flashCount
    for x,y in [(-1,0), (1, 0), (0,1), (0,-1), (-1,-1), (-1, 1), (1,-1), (1,1)]:
        data[i+x, j+y] += 1
        if data[i+x][j+y] > 9 and [i+x, j+y] not in flashes:
            flashes.append([i+x, j+y])
            flashCount += 1
            flash2(i+x, j+y)


for h in range(300): #each step
    add1(data)
    for i in range(numRow):
        for j in range(rowLen):
            flash(i+1, j+1)
    set0(i,j)
    if len(flashes) == 100:
        print("YEAH", h)
    flashes = []

print(flashCount,"!")
