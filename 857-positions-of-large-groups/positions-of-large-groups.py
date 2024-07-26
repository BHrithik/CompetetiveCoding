class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        l=0
        r=0
        prev = None
        for i in range(len(s)):
            if s[i] == prev:
                r+=1
            else:
                if r-l+1 >= 3:
                    res.append([l,r])
                l=i
                r=i
                prev=s[i]
        if r-l+1 >= 3:
            res.append([l,r])
        return res
