class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxWater = 0
        while l < r:
            a = r-l
            b = min(height[r],height[l])
            maxWater = max(maxWater,a*b)
            if height[l] < height[r]:
                l = l+1
            else:
                r = r-1
        return maxWater