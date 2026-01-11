class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxWater = 0
        while l < r:
            cur_water = min(height[l],height[r])*(r-l)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            maxWater = max(maxWater, cur_water)
        return maxWater