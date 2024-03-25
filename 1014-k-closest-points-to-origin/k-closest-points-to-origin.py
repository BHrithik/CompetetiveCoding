class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        em = []
        distDict = defaultdict(list)
        for i in points:
            num = abs((i[0]**2)+(i[1]**2))
            em.append((num,i[0],i[1]))
        em.sort()
        res = []
        for i in range(k):
            res.append([em[i][1],em[i][2]])
        return res