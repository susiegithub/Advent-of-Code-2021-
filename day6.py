with open("day6.txt") as file:
    data = file.read().split(",")

fishNum = len(data)
data = list(map(int, data))
counter = 0
cycleDay = []
for i in range(9):
    cycleDay.append(data.count(i))


for i in range(256):
    newFish = cycleDay[0]
    cycleDay.append(cycleDay.pop(0))
    cycleDay[6] += newFish
    cycleDay[8] = newFish

        
print(sum(cycleDay))

    

