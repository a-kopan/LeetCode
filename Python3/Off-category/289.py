#live cell dies if <2 neighbours
#live cell lives if neighbours==2 or neighbours==3
#live cell dies if >3 neighbours 

#dead cell ressurects if neighbours==3

def gameOfLife(board: list) -> None:
    next_state = []
    for row in board:
        next_state.append(row.copy())
    
    for x in range(0,len(board)):
        for y in range(0,len(board[0])):
            neighbours = []
            #fill the neighbours coords if they are in the board range
            for i in range(-1,2):
                row = x+i
                if row<0 or row>len(board)-1:
                    continue
                for j in range(-1,2):
                    column = y+j
                    if column<0 or column>len(board[0])-1: continue
                    elif (row,column)==(x,y): continue
                    elif board[row][column]==0: continue
                    else: neighbours.append((row,column))
            #check the ammount of alive neighbours and decide the next_state's cell
            #if the cell was alive
            if board[x][y] and not 1<len(neighbours)<4: next_state[x][y]=0
            #if the cell was dead
            elif len(neighbours)==3: next_state[x][y]=1
    board.clear()
    
    for row in next_state:
        board.append(row.copy())


if __name__=="__main__":
    board = [[0,1,0],
             [0,0,1],
             [1,1,1],
             [0,0,0]]
    print(board)
    gameOfLife(board)
    print(board)