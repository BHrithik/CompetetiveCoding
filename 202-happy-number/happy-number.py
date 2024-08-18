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
        while n != 1 and n not in seen:
            seen.add(n)
            n = getSum(n)
        return n==1
            
