class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        print(num)
        if num == 1:
            return 0
        s = 0
        while num != 1:
            if num % 2 == 0:
                s = s+1
                num = num//2
            else:
                s = s+1
                num = num +1
        return s