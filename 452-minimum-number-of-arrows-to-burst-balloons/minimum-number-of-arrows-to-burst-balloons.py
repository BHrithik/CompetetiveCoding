class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #[[10,16],[2,8],[1,6],[7,12]]
        #[[1,6], [2,8], [7,12], [10,16]]
        #[[2,6]
        count = 0
        points.sort()
        res = [points[0]]
        prevEnd = res[0][1]
        for i in range(1,len(points)):
            start, end = points[i]
            prevEnd = res[-1][1]
            if start <= prevEnd:
                res[-1][1] = min(prevEnd,end)
            else:
                res.append([start,end])
        return len(res)
