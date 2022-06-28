from re import L


res = 0
board = []

def printSol():
    print('Solution {}:'.format(res))
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=' ')
        print()

def validMove(board,row,col):
    i=col-1
    for i in range(n):
        if board[row][i]:
            return False
    
    i = row
    j = col
    while i>=0 and j>=0:
        if board[i][j]:
            return False
        i-=1
        j-=1
    i = row
    j = col
    while i<n and j>=0:
        if board[i][j]:
            return False
        i+=1
        j-=1
    return True
def solve(board,col):
    if col == n:
        global res
        res+=1
        printSol()
        return

    for i in range(n):
        if validMove(board,i,col):
            board[i][col]=1
            solve(board,col+1)
            board[i][col]=0
    
    return 


n=int(input('enter a number: ')) 
for i in range(n):
    board.append([])
    for j in range(n):
        board[-1].append(0)

solve(board, 0)
print('no of possible solutions: ', res)
