class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        def markSafe(i,j):
            if i >= 0 and i <= len(board)-1 and j >= 0 and j <= len(board[0])-1 and board[i][j] == "O":
                board[i][j] = "S"
                for di,dj in directions: markSafe(i+di,j+dj)
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if (i==0 or i==len(board)-1 or j==0 or j==len(board[i])-1) and board[i][j]=="O":
                    markSafe(i,j)
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                if board[i][j] == "S":
                    board[i][j] = 'O'
        print(board)
        

        