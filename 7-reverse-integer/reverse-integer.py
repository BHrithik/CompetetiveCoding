class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            ans = int(str(abs(x))[::-1])
            return 0 if ans > 2**31-1 else ans
        else:
            ans = -int(str(abs(x))[::-1])
            return 0 if ans < -2**31 else ans