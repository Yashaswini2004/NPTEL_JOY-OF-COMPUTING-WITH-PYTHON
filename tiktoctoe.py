import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'
def won(symbol):
    return check_row(symbol) or check_col(symbol) or check_diagnol(symbol)
def check_row(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,"won")
            return True
    return False
def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,"won")
            return True
    return False
def check_diagnol(symbol):
    if board[0][2]==board[1][1] and board[2][0]==board[1][1] and board[1][1]=='-':
        print(symbol,'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]=='-':
        print(symbol,'won')
        return True
    return False

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter the row-1 or 2 or 3"))
        col=int(input("Enter the row-1 or 2 or 3"))
        if row>0 and col>0 and row<9 and col<9 and board[row-1][col-1]=='-':
            break
        else:
            print("The invalid input,please enter again")
    board[row-1][col-1]=symbol
def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
                break
        if not(won(p1s)) and not(won(p2s)):
            print('DRAW')
play()