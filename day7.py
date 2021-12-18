with open("day7.txt") as file:
    data = file.read().split(",")
data = list(map(int, data))
fuelCounter = (sum(data))**5
counter = 0
for i in range(min(data), max(data)):
    myNums = []
    pos = i
    fuelCount= [abs(x-pos) for x in data]
    for x in fuelCount:
        counter = 0
        counter = (x*(x+1))/2
        myNums.append(counter)
    
    if fuelCounter > sum(myNums):
        fuelCounter = sum(myNums)
        bestpos = i

print(fuelCounter, bestpos)