class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorsum = 0
        for i in nums:
            xorsum ^= i
        bitDiff = 1
        while not bitDiff & xorsum:
            bitDiff = bitDiff << 1
        a ,b = 0, 0
        for i in nums:
            if bitDiff & i:
                a ^= i
            else:
                b ^= i
        return [a,b]
        

            