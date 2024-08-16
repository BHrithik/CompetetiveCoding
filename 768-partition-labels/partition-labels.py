class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charDict = {}
        for i in range(0,len(s)):
            charDict[s[i]] = i
        cur_max = charDict[s[0]]
        res = []
        cur_sum = 0
        for r in range(0,len(s)):
            cur_max = max(cur_max,charDict[s[r]])
            if r == cur_max:
                res.append(r+1-sum(res))
        return res