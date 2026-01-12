class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_count = {}
        res = 0
        maxF = 0
        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r],0) + 1
            maxF = max(char_count[s[r]],maxF)
            if r-l+1 - maxF > k:
                char_count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res