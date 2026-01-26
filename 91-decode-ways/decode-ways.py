class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0' or "00" in s:
            return 0
        n = len(s)
        memo = {}
        def helper(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]

            ways = helper(i + 1)

            if i + 1 < n:
                two = int(s[i:i+2])
                if 10 <= two <= 26:
                    ways += helper(i + 2)
            memo[i] = ways
            return ways
        return helper(0)