class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        length = n*2
        res = []
        def valid(s):
            stack = []
            for char in s:
                if char == '(':
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0
        def helper(s):
            if len(s) == length:
                if valid(s):
                    res.append(s)
                return
            if s.count('(') < n:
                helper(s + '(')
            if s.count(')') < s.count('('):
                helper(s + ')')
        helper("")
        return res