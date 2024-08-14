class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(i,j):
            return (i*i)+(j*j)
        points = [(getDistance(i,j),i,j) for i,j in points]
        heapq.heapify(points)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(points)[1:])
        return ans
        