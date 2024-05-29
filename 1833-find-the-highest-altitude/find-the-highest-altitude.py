class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight = -999999999999999
        curr = 0
        for i in gain:
            maxHeight = max(maxHeight,curr)
            curr = curr + i
        maxHeight = max(maxHeight,curr)
        return maxHeight