class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        get_opposite = {"{":"}","(":")","[":"]"}
        i = 0
        while i < len(s):
            if s[i] in get_opposite:
                stack.append(s[i])
            else:
                if stack and s[i] in get_opposite.values() and s[i] == get_opposite[stack[-1]]:
                    stack.pop()
                else:
                    return False
            i += 1
        if stack:
            return False
        return True