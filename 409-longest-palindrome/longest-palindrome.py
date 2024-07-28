class Solution:
    def longestPalindrome(self, s: str) -> int:
        A = Counter(s)
        ans = 0
        oddPresent = False
        for i in A.values():
            if i%2 == 0:
                ans += i
            else:
                oddPresent = True
                ans += i-1
        return ans+1 if oddPresent else ans
        