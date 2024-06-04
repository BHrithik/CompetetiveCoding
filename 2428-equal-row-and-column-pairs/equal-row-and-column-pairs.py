class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        grid2 = [[0]*n for _ in range(n)]
        print(grid2)
        for i in range(n):
            for j in range(n):
                grid2[i][j] = grid[j][i]
        print(grid2)
        count = 0
        for i in grid:
            for j in grid2:
                if i == j:
                    count = count + 1
        return count