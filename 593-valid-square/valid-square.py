import math

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p1,p2):
            return math.dist(p1,p2)
        
        distances = set()
        distances.add(dist(p1,p2))
        distances.add(dist(p1,p3))
        distances.add(dist(p1,p4))
        distances.add(dist(p2,p4))
        distances.add(dist(p2,p3))
        distances.add(dist(p3,p4))
        points = [p1,p2,p3,p4]
        dummy = []
        for i in points:
            if i not in dummy:
                dummy.append(i)
        if len(dummy) == 4:
            return len(distances) == 2
        else:
            return False