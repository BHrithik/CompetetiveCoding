class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif s[i] == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif s[i] == "]":
                if stack and stack[-1] == "[":
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