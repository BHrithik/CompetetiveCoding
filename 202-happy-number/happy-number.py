class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            res = []
            cur_sum = 0
            while n!= 0:
                digit = n%10
                cur_sum += digit*digit
                n = n//10
            return cur_sum
        seen = set()
        while n not in seen:
            seen.add(n)
            n = getSum(n)
            if n == 1:
                return True
        return False