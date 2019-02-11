board = []
N=4
def setboard():
    l = []
    for i in range(N):
        l.append(0)
        board.append(l)
def viewboard():
    for i in range(N):
        for j in range(N):
            print(board[i][j] ,end = " ")
        print()
setboard()
viewboard()
def place_q():
    place_q_helper()
