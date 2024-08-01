class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.max_len = 0
        def fromMiddle(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > self.max_len:
                    self.max_len = r-l+1
                    self.res = s[l:r+1]
                l -= 1
                r += 1
        for i in range(0,len(s)):
            fromMiddle(i,i)
            fromMiddle(i,i+1) 
        return self.res