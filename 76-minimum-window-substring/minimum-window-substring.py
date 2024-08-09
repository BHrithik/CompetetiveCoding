class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        tCount = Counter(t)
        sCount = {}
        l = 0
        minLen = float('inf')
        minRes = ""
        have = 0
        need = len(tCount)
        for r in range(0,len(s)):
            if s[r] in tCount:
                sCount[s[r]] = sCount.get(s[r],0)+1
                if sCount[s[r]] == tCount[s[r]]:
                    have += 1
                while have == need:
                    if r-l+1 < minLen:
                        minLen = r-l+1
                        minRes = s[l:r+1]
                    if s[l] in sCount:
                        sCount[s[l]] -= 1
                    if s[l] in sCount and sCount[s[l]] < tCount[s[l]]:
                        have -= 1
                    l += 1
        return minRes
            
        