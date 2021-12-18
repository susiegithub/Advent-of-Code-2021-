from collections import Counter
with open("day5.txt") as file:
    data = file.readlines()

points = []
def getPoints(p1, p2):
    global points
    x1, x2 = p1[0], p2[0]
    y1, y2 = p1[1], p2[1]
    

    x,y = x1,y1
    
    while x != x2 or y != y2:
        points.append((x,y))
        if x < x2: 
            x+=1
        elif x > x2:
            x-=1
            
        if y < y2:
            y+=1
        elif y > y2:
            y-=1
    points.append((x2,y2))
    return list(points)
    
def removeComma(data):
    return list(map(int, data.split(",")))

def coordSplit(line):
    global p1,p2
    p1, p2 = line.split("->")

for line in data:
    coordSplit(line)
    p1, p2 = removeComma(p1), removeComma(p2)
    getPoints(p1,p2)

mycount = Counter(points)
mycount = list(mycount.values())
myCount = [1 for x in mycount if x>=2]
print(sum(myCount))
