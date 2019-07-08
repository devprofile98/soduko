import numpy as np
board=np.zeros((9,9),np.integer)
boward=[[7,8,0,4,0,0,1,2,0],
       [6,0,0,0,7,5,0,0,9],
       [0,0,0,6,0,1,0,7,8],
       [0,0,7,0,4,0,2,6,0],
       [0,0,1,0,5,0,9,3,0],
       [9,0,4,0,6,0,0,0,5],
       [0,7,0,3,0,0,0,1,2],
       [1,2,0,0,0,7,4,0,0],
       [0,4,9,2,0,6,0,0,7]
    ]

def backtrack(board):
    Position = FindEmpty(board)
    if Position == None:
        return True
    else:
        x , y = Position
        #print (x,y)
    for i in range(1,10):
        board[x][y] = i
        #print (board)
        if promising(board,x,y):
            
            if backtrack(board):
                return True
        board[x][y]=0




def promising(board,i,j):
    
    
    switch = True
    #print (j)
    for x in range(0,j+1):
        for y in range(0,j+1):
            if x!=y and board[i][x] == board[i][y] and board[i][x]!=0:
                switch = False
    for x in range(0,i+1):
        for y in range(0,i+1):
            if x!=y and board[x][j]==board[y][j] and board[x][j]!=0:
                switch = False
                
    
                
    include =[0,1,2,3,4,5,6,7,8,9]
    for x in range(i-(i%3),(i-(i%3))+3):
        for y in range(j-(j%3),(j-(j%3))+3):
            
            if include[int(board[x][y])] == None:
                #print ('000000000000000000000000000000000000')

                #print (int(board[x][y]))
                switch = False
                break
            if int(board[x][y])!=0:
                include[int(board[x][y])] = None
    #print (switch)
    return switch
            
def FindEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None

def PrintBoard(board):
    for i in range(9):
        print (board[i])

backtrack(board)

PrintBoard(board)
