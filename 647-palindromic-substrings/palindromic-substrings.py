class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0
        def exploreFromMiddle(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.res += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            exploreFromMiddle(i,i)
            exploreFromMiddle(i,i+1)
        return self.res