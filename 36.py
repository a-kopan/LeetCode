board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
    #check rows
    #create a map for counting elements in board and if some count>1, return False
    columnMap = {i:[] for i in range(0,9)}
    boxMap = {i:None for i in range(0,9)}
    #check rows and at the same time fill columnMap and boxMap
    for row in range(0,9):
        rowCountMap = {}
        for column in range(0,9):
            rowCountMap.setdefault(board[row][column],0)
            rowCountMap[board[row][column]]+=1
            columnMap[column].append(board[row][column])
            
        for pair in rowCountMap.items():
            if pair[1]>1 and pair[0]!='.':
                return False
    #check columns
    for column in columnMap.values():
        columnCountMap = {}
        for val in column:
            columnCountMap.setdefault(val,0)
            columnCountMap[val]+=1
        for pair in columnCountMap.items():
            if pair[1]>1 and pair[0]!='.':
                return False
    #check boxes
    box_ind = 0
    for row in (0,3,6):
        for column in (0,3,6):
            box = [board[x][y] for x in range(row,row+3) for y in range(column,column+3)]
            boxMap[box_ind] = box
            box_ind+=1
    for arr in [pair[1] for pair in boxMap.items()]:
        temp_map = {}
        for elem in arr:
            temp_map.setdefault(elem,0)
            temp_map[elem]+=1
        for pair in temp_map.items():
            if pair[1]>1 and pair[0]!='.':
                return False
    return True

print(isValidSudoku(board2))