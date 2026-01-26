class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        memo = {n: 1}
        def helper(i):
            if i in memo:
                return memo[i]
            if s[i] == "0":
                return 0
            res = helper(i + 1)
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += helper(i + 2)
            memo[i] = res
            return res
        return helper(0)