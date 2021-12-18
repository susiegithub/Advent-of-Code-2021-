with open("day10.txt") as file:
    data = file.read().split("\n")
    
incorrectDict = {
"(": {"]":57, "}":1197 , ">":25137 },
"[":{")":3, "}": 1197, ">":25137 },
 "{": {")":3 , "]":57, ">": 25137},
"<": {")": 3, "]": 57, "}": 1197} 
}

correctDict = {
"(": ")",
"[": "]",
"{": "}",
"<": ">"
}

score = {
"(": 1,
"[": 2,
"{": 3,
"<": 4
}
opening = ("(", "[", "{", "<")
inputList = []
#counter = 0 
scoreList = []
corrupt = []
data2= []
completeList = []
for i in range(len(data)):
    inputList = []
    for h in range(len(data[i])):
        if data[i][h] in opening:
            inputList.append(data[i][h])
        else: #closing symbol
            inputList.reverse()
            #counter += incorrectDict[inputList[0]].get(data[i][h],0) for part 1
            if correctDict.get(inputList[0]) != data[i][h]: #if corrupt
                corrupt.append(i)
            inputList.pop(0)
            inputList.reverse()
            
        if len(inputList) !=0 and h == (len(data[i]))-1 and i not in corrupt:
            inputList.reverse()
            completeList.append(inputList)

for i in range(len(completeList)):
    score1 = 0
    for x in completeList[i]:
        score1 *= 5 
        score1 += (score.get(x))
    scoreList.append(score1)

scoreList = sorted(scoreList)
index = int((len(scoreList))/2)
print(scoreList[index]) 