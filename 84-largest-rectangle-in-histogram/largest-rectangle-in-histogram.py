class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        res = 0
        for i in range(0,len(heights)):
            height = heights[i]
            while stack and stack[-1][0] > height:
                h, _ = stack.pop()
                width = i if not stack else i - stack[-1][1] - 1
                res = max(res,h*width)
            stack.append((height,i))
        return res