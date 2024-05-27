class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        memo = {}
        def dfs(movesLeft, curRow, curCol):
            if (movesLeft, curRow, curCol) in memo:
                return memo[(movesLeft, curRow, curCol)]
            if curRow < 0 or curRow >= m or curCol < 0 or curCol >= n:
                return 1
            if movesLeft == 0:
                return 0
            paths = (
                dfs(movesLeft - 1, curRow - 1, curCol) +
                dfs(movesLeft - 1, curRow + 1, curCol) +
                dfs(movesLeft - 1, curRow, curCol - 1) +
                dfs(movesLeft - 1, curRow, curCol + 1)
            ) % MOD
            memo[(movesLeft, curRow, curCol)] = paths
            return paths
        return dfs(maxMove, startRow, startColumn)