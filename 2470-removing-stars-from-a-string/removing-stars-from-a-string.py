class Solution:
    def removeStars(self, s: str) -> str:
        starCount = 0
        letterCount = 0
        ans = ""
        s=s[::-1]
        for i in range(0,len(s)):
            if s[i] == "*":
                starCount += 1
            else:
                if starCount == 0:
                    ans+=s[i]
                else:
                    starCount -= 1
        return ans[::-1]