import re
import numpy as np
import sys
with open("day4.txt") as file:
    data = file.read()
order = data.split("\n")[0]
order = order.split(",")
orderlen = len(order)
order = list(map(str, order))


boards = re.split(r"[\n, ]", data)[orderlen:]
boards = [x for x in boards if x!='']

boards2 = np.array(boards)
boards = boards2.reshape(int(len(boards)/5),5)
numBoards = int(len(boards)/5)
boards2= boards.reshape(numBoards,5,5)
breakOutFlag = False
winningBoard = []
wonindices = []

def column(data):
    for x in np.all(data == "X", axis=1):
        if x == True:
            print("YAY COLUMN")
            print(n)
            global wonindices, winningBoard
            for x in np.nditer(data):
                if x!="X":
                    winningBoard.append(str(x))
            wonindices.append(n)
            wonindices = list(dict.fromkeys(wonindices)) 
            if len(wonindices) == len(boards2):
                global breakOutFlag
                breakOutFlag = True
            else:
                winningBoard = []
            
            
#winningBoard = [str(x) for x in np.nditer(data) if x!="X"]

def row(data):
    for x in np.all(data == "X", axis=0):
        if x == True:
            print("YAY ROW")
            print(n)
            global breakOutFlag, wonindices, winningBoard
            for x in np.nditer(data):
                if x!="X":
                    winningBoard.append(str(x))
            wonindices.append(n)
            wonindices = list(dict.fromkeys(wonindices)) 
            if len(wonindices) == len(boards2):
                breakOutFlag = True
            else:
                winningBoard = []
                
for number in order: #ew this code
    for i in range(len(boards2)): #selects board
        for j in range(len(boards2[i])): #selects row
            for k in range(len(boards2[i][j])): #selects element
                if boards2[i,j,k] == number:
                    boards2[i,j,k] = "X"
                
    for n in range(len(boards2)): #one board selected
        row(boards2[n])
        if breakOutFlag == True:
            print("The winner was:",winningBoard)
            winningBoardfinal = list(map(int, winningBoard))
            print(int(number))
            print("SUM:",(sum(winningBoardfinal))*int(number))
            sys.exit()


    for n in range(len(boards2)): #one board selected
        column(boards2[n])
        if breakOutFlag == True:
            print("The winner was:",winningBoard)
            winningBoardfinal = list(map(int, winningBoard))
            print("SUM:",(sum(winningBoardfinal))*int(number))
            sys.exit()

        