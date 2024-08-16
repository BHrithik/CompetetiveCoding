class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
        x_str = int(str(abs(x))[::-1])
        if x_str > 2**31-1 or x_str < -2**31:
            return 0
        return int(x_str) if not negative else -int(x_str)