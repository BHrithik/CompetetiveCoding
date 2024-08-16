class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        stackDict = {")":"(","}":"{","]":"["}
        for i in s:
            if i in stackDict:
                if stack and stack[-1] == stackDict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True