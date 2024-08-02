class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[float('inf')]*n for _ in range(0,m)]
        for i in range(m):
            matrix[i][n-1] = 1
        for i in range(n):
            matrix[m-1][i] = 1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                matrix[i][j] = matrix[i+1][j]+matrix[i][j+1]
        print(matrix)
        return matrix[0][0]