import itertools
with open("day8.txt") as file:
    data = file.read().split("\n")

uniqueNum = [2,4,3,7]
counter = 0
newdata = []
data = [x.split("|") for x in data]
data = list(itertools.chain(*data))

def split(word):
    return list(word)

for i in range(len(data)):
    if data[i] != '': 
        newdata.append(data[i])

newdata2 = [x.split() for x in newdata]
newdata2 = list(itertools.chain(*newdata2))

potVal = {
"a": None,
"b":None,
"c":None,
"d":None,
"e":None,
"f":None,
"g":None
}

for x in newdata2:
    letters = split(x)
    if len(x) == 2:
        potVal.update({"c":letters})
        potVal.update({"g":letters})
        potVal["c"] = list(dict.fromkeys(potVal["c"]))
        potVal["g"] = list(dict.fromkeys(potVal["g"]))
    elif len(x) == 3:
        potVal.update({"a":letters})
        potVal.update({"c":letters})
        potVal.update({"f":letters})
        potVal["a"] = list(dict.fromkeys(potVal["a"]))
        potVal["c"] = list(dict.fromkeys(potVal["c"]))
        potVal["f"] = list(dict.fromkeys(potVal["f"]))


# for i in range(1, len(data),2): #selecting for only the output values
#     newdata.append(data[i])
# 
# print(newdata)
# newdata = [x.split() for x in newdata] # splits elements by space
# =============================================================================
#newdata = list(itertools.chain(*newdata)) #flattens array


#for x in newdata:
#    if len(x) in uniqueNum:
        #counter +=1
 
#print(counter)
 
