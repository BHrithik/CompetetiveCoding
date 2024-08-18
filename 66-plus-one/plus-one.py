class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        digits = digits[::-1]
        for i in range(0,len(digits)):
            num += digits[i]*(10**i)
        print(num)
        return [int(i) for i in str(num+1)]