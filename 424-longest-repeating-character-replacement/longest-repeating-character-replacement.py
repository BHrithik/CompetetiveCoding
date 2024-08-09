class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        cur_s = defaultdict(int)
        res = 0
        maxF = 0
        for r in range(0,len(s)):
            cur_s[s[r]] += 1
            maxF = max(cur_s[s[r]],maxF)
            while r-l+1 - maxF > k:
                cur_s[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res
