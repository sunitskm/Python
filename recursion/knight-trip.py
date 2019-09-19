#cerner_2^5_2019
import sys
board = []
moves = []
#total = 64
#c = 1
def setboard():
    for i in range(8):
        row = []
        for(j) in range(8):
            row.append(0)
        board.append(row)
def viewboard():
    for i in range(8):
        for j in range(8):
            print(board[i][j],end = "   ")
        print()
    #print(board)
def populate_moves():
    moves.append([-2,1])
    moves.append([-1,2])
    moves.append([-2,-1])
    moves.append([-1,-2])
    moves.append([1,-2])
    moves.append([1,2])
    moves.append([2,-1])
    moves.append([2,1])

def print_moves():
    for i in range(8):
        for j in range(2):
            print(moves[i][j],end=" ")
        print()
def isValid(r,c,k):
    step_r = moves[k][0]
    step_c = moves[k][1]
    if(r+step_r>=0 and r+step_r<=7 and c+step_c>=0 and c+step_c<=7):
        if(board[r+step_r][c+step_c]==0):
            return True
    return False

def start_tour(i,j):
    setboard()
    #viewboard()
    populate_moves()
    board[i][j]=1
    start_tour_helper(i,j,64,2)

def start_tour_helper(i,j,total,c):
    #print("start_tour_helper( "+str(i)+","+str(j)+","+str(total)+","+str(c)+")")
    if(total==1):
        print("Hello")
        viewboard()
        sys.exit(0)
    else:
        for k in range(8):
            if(isValid(i,j,k)):
                #print("start_tour_helper( "+str(i)+","+str(j)+","+str(total)+","+str(c)+")")
                board[i+moves[k][0]][j+moves[k][1]] = c
                start_tour_helper(i+moves[k][0],j+moves[k][1],total-1,c+1)
                board[i+moves[k][0]][j+moves[k][1]] = 0
start_tour(0,0)
