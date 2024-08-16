class Solution:
    def checkValidString(self, s: str) -> bool:
        leftstack = []
        starstack = []
        stars = 0
        for i in range(0,len(s)):
            if s[i] == "(":
                leftstack.append(i)
            elif s[i] == "*":
                starstack.append(i)
            else:
                if leftstack:
                    leftstack.pop()
                elif starstack:
                    starstack.pop()
                else:
                    return False
        while leftstack and starstack:
            if leftstack[-1] < starstack[-1]:
                leftstack.pop()
                starstack.pop()
            else:
                return False
        return False if leftstack else True