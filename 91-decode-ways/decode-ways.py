class Solution:
    def numDecodings(self, s: str) -> int:
        # #12106
        # res = 0
        cache = {}
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in cache:
                return cache[i]
            cache[i] = dfs(i+1)
            if i+1 < len(s) and int(s[i] + s[i+1]) <= 26:
                cache[i] += dfs(i+2)
            return cache[i]
        return dfs(0)
        # val1, val2 = 0, 0
        # for i in range(len(s)):
            
        dp = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            if i+1 < len(s) and int(s[i]+s[i+1]) <= 26:
                res += dfs(i+2)
            dp[i] = res
            return dp[i]
        return dfs(0)


            










