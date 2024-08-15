class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        self.maxLen = 0
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            length = 1
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                    length = max(length, 1 + dfs(x, y))
            cache[(i, j)] = length
            return length
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.maxLen = max(self.maxLen,dfs(i,j))
        return self.maxLen
