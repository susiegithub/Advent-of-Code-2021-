import re
import numpy as np
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
def column(data):
    for x in np.all(data == "X", axis=1):
        if x == True:
            print("YAY COLUMN")
            global breakOutFlag 
            breakOutFlag = True
            for x in np.nditer(data):
                if x!="X":
                    winningBoard.append(str(x))
        
#winningBoard = [str(x) for x in np.nditer(data) if x!="X"]

def row(data):
    for x in np.all(data == "X", axis=0):
        if x == True:
            print("YAY ROW")
            global breakOutFlag 
            breakOutFlag = True
            winningBoard = [x for x in np.nditer(data) if x!="X"]


for number in order: #ew this code
    for i in range(len(boards2)): #selects board
        for j in range(len(boards2[i])): #selects row
            for k in range(len(boards2[i][j])): #selects element
                if boards2[i,j,k] == number:
                    boards2[i,j,k] = "X"
                
    for board in boards2:
        column(board)
        row(board)

        
    if breakOutFlag == True:
        print("The winner was:",winningBoard)
        winningBoardfinal = list(map(int, winningBoard))
        print("SUM:",(sum(winningBoardfinal))*int(number))
        break
     
