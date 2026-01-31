class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_dist_points = []
        for x, y in points:
            dist = (x*x)+(y*y)
            new_dist_points.append([dist,x,y])
        heapq.heapify(new_dist_points)
        res = []
        while k > 0:
            dist,x,y = heapq.heappop(new_dist_points)
            res.append((x,y))
            k -= 1
        return res
