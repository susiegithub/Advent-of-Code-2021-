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
    data[i-1][j] += 1 #above
    data[i+1][j] += 1 #below
    data[i][j+1] += 1 #right
    data[i][j-1] += 1 #left
    
    data[i-1][j-1] += 1 #top left diagonal
    data[i-1][j+1] += 1 #top right diagonal
    data[i+1][j-1] += 1 #bottom left diagonal
    data[i+1][j+1] += 1 #bottom right diagonal
    
    if data[i-1][j] > 9: #above
        if [i-1, j] not in flashes:
            flashes.append([i-1,j])
            flashCount += 1
            flash2(i-1, j)
            
    if data[i+1][j] > 9: #below
        if [i+1, j] not in flashes:
            flashes.append([i+1, j])
            flashCount += 1
            flash2(i+1, j)
            
    if data[i][j+1] > 9: #right
        if [i, j+1] not in flashes:
            flashes.append([i, j+1])
            flashCount += 1
            flash2(i, j+1)
            
    if data[i][j-1] > 9: #left
        if [i, j-1] not in flashes:
            flashes.append([i, j-1])
            flashCount += 1
            flash2(i, j-1)
            
    if data[i-1][j-1] > 9: #TLD
        if [i-1, j-1] not in flashes:
            flashes.append([i-1,j-1])
            flashCount += 1
            flash2(i-1, j-1)
            
    if data[i-1][j+1] > 9: #TRD
        if [i-1, j+1] not in flashes:
            flashes.append([i-1, j+1])
            flashCount += 1
            flash2(i-1, j+1)
            
    if data[i+1][j-1] > 9: #BLD
        if [i+1, j-1] not in flashes:
            flashes.append([i+1, j-1])
            flashCount += 1
            flash2(i+1, j-1)
            
    if data[i+1][j+1] > 9: #BRD
        if [i+1, j+1] not in flashes:
            flashes.append([i+1, j+1])
            flashCount += 1
            flash2(i+1, j+1)
            

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
    