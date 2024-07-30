class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for i in range(0,len(spells)):
            l = 0
            r = len(potions)-1
            pos = len(potions)
            while l<=r:
                mid = (l+r)//2
                if potions[mid]*spells[i] >= success:
                    pos = mid
                    r = mid-1
                else:
                    l = mid+1
            res.append(len(potions)-pos)
        return res