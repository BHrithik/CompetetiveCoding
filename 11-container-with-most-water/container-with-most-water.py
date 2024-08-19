class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        H = max(height)

        while left < right:
            W = (right - left)

            if H*W <= maxArea:
                return maxArea
            
            currentArea = min(height[left], height[right]) * W
            maxArea = max(maxArea, currentArea)
            
            if height[left] == height[right]:
                left += 1
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea