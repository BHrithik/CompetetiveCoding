class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [['.']*n for _ in range(n)]
        def dfs(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
            for c in range(n):
                if c in col or c+r in posDiag or r-c in negDiag:
                    continue
                col.add(c)
                posDiag.add(c+r)
                negDiag.add(r-c)
                board[r][c] = 'Q'
                dfs(r+1)
                col.remove(c)
                posDiag.remove(c+r)
                negDiag.remove(r-c)
                board[r][c] = '.'
        dfs(0)
        return res