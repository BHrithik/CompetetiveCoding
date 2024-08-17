class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        freeSpace = set()
        def dfs(i,j):
            if i not in range(ROWS) or j not in range(COLS) or board[i][j] == "X" or (i,j) in freeSpace:
                return
            freeSpace.add((i,j))
            for di, dj in directions:
                dfs(di+i,dj+j)
        for i in range(len(board)):
            dfs(i,0)
            dfs(i,COLS-1)
        for j in range(len(board[0])):
            dfs(0,j)
            dfs(ROWS-1,j)
        print(freeSpace)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i,j) not in freeSpace:
                    board[i][j] = "X"
        return board
                




















        # directions = [(1,0),(0,1),(0,-1),(-1,0)]
        # def markSafe(i,j):
        #     if i >= 0 and i <= len(board)-1 and j >= 0 and j <= len(board[0])-1 and board[i][j] == "O":
        #         board[i][j] = "S"
        #         for di,dj in directions: markSafe(i+di,j+dj)
        # for i in range(0,len(board)):
        #     for j in range(0,len(board[i])):
        #         if (i==0 or i==len(board)-1 or j==0 or j==len(board[i])-1) and board[i][j]=="O":
        #             markSafe(i,j)
        # for i in range(0,len(board)):
        #     for j in range(0,len(board[0])):
        #         if board[i][j] == "O":
        #             board[i][j] = 'X'
        #         if board[i][j] == "S":
        #             board[i][j] = 'O'
        # print(board)
        

        