class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0] * n for _ in range(m)]
        for i in range(0,len(board)):
            board[i][n-1] = 1
        for i in range(0,len(board[0])):
            board[m-1][i] = 1
        for i in range(len(board)-2,-1,-1):
            for j in range(len(board[0])-2,-1,-1):
                if i+1 > len(board)-1:
                    sum1 = 0
                else:
                    sum1 = board[i+1][j]
                if j+1 > len(board[0])-1:
                    sum2 = 0
                else:
                    sum2 = board[i][j+1]
                board[i][j] = sum1 + sum2

        return board[0][0]