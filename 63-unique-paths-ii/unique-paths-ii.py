class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        pathCounter = {(m-1,n-1): 1}
        def dfs(i,j):
            if i == m or j == n or obstacleGrid[i][j]:
                return 0
            if (i,j) in pathCounter:
                return pathCounter[(i,j)]
            pathCounter[(i,j)] = dfs(i+1,j) + dfs(i,j+1)
            return pathCounter[(i,j)]
        return dfs(0,0)
