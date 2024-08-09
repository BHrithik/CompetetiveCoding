class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sCounter = Counter(s1)
        window = len(s1)
        s2Counter = Counter(s2[:window])
        if s2Counter == sCounter:
            return True
        l = 0
        for r in range(window,len(s2)):
            s2Counter[s2[r]] = s2Counter.get(s2[r],0)+1
            s2Counter[s2[l]] -= 1
            if s2Counter[s2[l]] == 0:
                del s2Counter[s2[l]]
            if s2Counter == sCounter:
                return True
            l+=1
        return False

        