class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        r = points[0]
        for i in range(1,ROWS):
            nextRows = points[i].copy()
            left, right = [0]*COLS, [0]*COLS
            left[0] = r[0]
            right[-1] = r[-1]
            for c in range(1,COLS):
                left[c] = max(r[c],left[c-1]-1)
            for c in range(COLS-2,-1,-1):
                right[c] = max(r[c],right[c+1]-1)

            for c in range(0,COLS):
                nextRows[c] = nextRows[c] + max(left[c],right[c])
            r = nextRows
        return max(r)
            