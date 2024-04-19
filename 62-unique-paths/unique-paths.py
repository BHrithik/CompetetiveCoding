class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]= grid[i-1][j]+grid[i][j-1]
        return grid[-1][-1]
        # A = defaultdict(int)
        # for i in range(m):
        #     A[(i, n-1)] = 1
        # for j in range(n):
        #     A[(m-1, j)] = 1
        # for i in range(m-2, -1, -1):
        #     for j in range(n-2, -1, -1):
        #         A[(i, j)] = A[(i+1, j)] + A[(i, j+1)]        
        # print(A)
        # return A[(0, 0)]