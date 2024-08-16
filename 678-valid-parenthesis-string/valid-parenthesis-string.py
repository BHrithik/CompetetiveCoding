class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0
        for i in s:
            if i == "(":
                leftMin += 1
                leftMax += 1
            elif i == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax <0:
                return False
            if leftMin <0:
                leftMin = 0
        return leftMin == 0

        # leftstack = []
        # starstack = []
        # stars = 0
        # for i in range(0,len(s)):
        #     if s[i] == "(":
        #         leftstack.append(i)
        #     elif s[i] == "*":
        #         starstack.append(i)
        #     else:
        #         if leftstack:
        #             leftstack.pop()
        #         elif starstack:
        #             starstack.pop()
        #         else:
        #             return False
        # while leftstack and starstack:
        #     if leftstack[-1] < starstack[-1]:
        #         leftstack.pop()
        #         starstack.pop()
        #     else:
        #         return False
        # return False if leftstack else True