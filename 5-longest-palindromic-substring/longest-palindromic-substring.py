class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        for length in range(n, 0, -1):
            for start in range(n - length + 1):
                substring = s[start:start+length]
                if substring == substring[::-1]:
                    return substring
        return substring[0]
