class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        stackDict = {")":"(","}":"{","]":"["}
        while i < len(s):
            if s[i] in stackDict:
                if stack and stack[-1] == stackDict[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
            i += 1
        if stack:
            return False
        else:
            return True