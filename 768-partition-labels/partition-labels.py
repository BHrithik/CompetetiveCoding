class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charDict = {}
        for i in range(0,len(s)):
            char = s[i]
            if char not in charDict:
                charDict[char] = i
            charDict[char] = i
        cur_max = charDict[s[0]]
        res = []
        for r in range(0,len(s)):
            cur_max = max(cur_max,charDict[s[r]])
            if r == cur_max:
                res.append(r+1-sum(res))
        return res
        # while r < len(s):
        #     if r == charDict[cur_char]:
        #         res.append(cur_s)
        #         cur_s = ""
        #     else:
        #         cur_s += s[r]
        #         if s[r] != cur_char:
        #             if charDict[s[r]] > charDict[cur_char]:
        #                 cur_char = s[r]
        #     r += 1
        # return res

        
