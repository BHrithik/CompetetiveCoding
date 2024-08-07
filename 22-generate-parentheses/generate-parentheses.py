class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        length = n*2
        res = set()
        cache = defaultdict(list)
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
                if s not in res and valid(s):
                    res.add(s)
                return
            cache[len(s)].append(s)
            if cache[length-len(s)]:
                for each in cache[length-len(s)]:
                    helper(s+each)
            if s.count('(') < n:
                helper(s + '(')
            if s.count(')') < s.count('('):
                helper(s + ')')
        helper("")
        return list(res)