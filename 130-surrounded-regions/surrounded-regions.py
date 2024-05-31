class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [[1,0],[0,1],[0,-1],[-1,0]]
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def markSafe(i,j):
            if (i,j) in visited:
                return
            if i >= 0 and i <= rows-1 and j >= 0 and j <= cols-1 and board[i][j] == "O":
                board[i][j] = "S"
                visited.add((i,j))
                markSafe(i+1,j)
                markSafe(i-1,j)
                markSafe(i,j+1)
                markSafe(i,j-1)

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
        

        