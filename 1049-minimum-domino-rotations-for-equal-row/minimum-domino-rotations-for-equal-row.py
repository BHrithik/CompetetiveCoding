class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        topCounter = defaultdict(lambda:set())
        bottomCounter = defaultdict(lambda:set())
        n = len(tops)
        allNums = set()
        for i in range(n):
            topCounter[tops[i]].add(i)
            bottomCounter[bottoms[i]].add(i)
            allNums.add(bottoms[i])
            allNums.add(tops[i])
        res = float('inf')
        for i in list(allNums):
            mapTop = topCounter[i]
            mapBottom = bottomCounter[i]
            if len(mapTop | mapBottom) == n:
                if len(mapTop) > len(mapBottom):
                    return n - len(mapTop)
                else:
                    return n - len(mapBottom)
        return -1