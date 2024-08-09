class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_index = {}
        ans = 0
        left = 0
        for right in range(0,n):
            if s[right] in char_index:
                if char_index[s[right]] >= left:
                    left = char_index[s[right]]+1
            char_index[s[right]] = right
            ans = max(right-left+1,ans)
        return ans
                