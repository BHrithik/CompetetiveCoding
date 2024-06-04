# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        nL = 1
        nM = n
        k = (nL+nM)//2
        g = guess(k)
        while g!= 0:
            if g == -1:
                nM = k-1
            else:
                nL = k+1
            k = (nL+nM)//2
            g = guess(k)
        return k