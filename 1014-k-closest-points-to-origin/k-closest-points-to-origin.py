class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(i,j):
            return math.sqrt((i*i)+(j*j))
        return sorted(points,key=lambda x: getDistance(x[0],x[1]))[:k]