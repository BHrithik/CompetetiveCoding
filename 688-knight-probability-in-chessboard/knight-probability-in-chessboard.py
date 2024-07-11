class Solution:
    def dp(self, x, y, n, visited, k,directions):
        if k<0:
            return 1
        if (x<0 or x>=n) or (y<0 or y>=n):
            return 0
        if (x,y,k) in visited:
            return visited[(x,y,k)]
        ans = 0
        for x_move, y_move in directions:
            ans+= self.dp(x+x_move, y+y_move, n, visited,k-1, directions)*1/8
        visited[(x,y,k)] = ans
        return ans

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(1,2),(2,1),(-1,-2),(-2,-1),(1,-2),(-2,1),(-1,2),(2,-1)]
        return self.dp(row,column,n,{},k,directions)