class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        maxLeft = height[l]
        maxRight = height[r]
        water = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft,height[l])
                water += max(0,maxLeft-height[l])
            else:
                r -= 1
                maxRight = max(maxRight,height[r])
                water += max(0,maxRight-height[r])
        return water
                
        n = len(height)
        # l = 0
        # r = n-1
        # water = 0
        # leftmax,rightmax = height[l], height[r]
        # while l < r:
        #     if leftmax < rightmax:
        #         l += 1
        #         leftmax = max(leftmax,height[l])
        #         water += max(0,leftmax-height[l])
        #     else:
        #         r -= 1
        #         rightmax = max(rightmax,height[r])
        #         water += max(0,rightmax-height[r])
        # return water

                
        # matrix = [[0]*n for _ in range(max(height))]
        # print(matrix)      
        # for i in range(0,len(height)):
        #     for j in range(0,height[i]):
        #         matrix[j][i] = 1
        # matrix = matrix
        # water = 0
        # for i in range(max(height)):
        #     matrix = [1 if wall > i else 0 for wall in height]
        #     if sum(matrix) == 1:
        #         continue
        #     leftFound = False
        #     for j in range(n):
        #         if leftFound and matrix[j] == 0 and sum(matrix[j:]) > 0:
        #             water += 1
        #             # matrix[j] = "W"
        #         if not leftFound and matrix[j] == 1:
        #             leftFound = True
        #     # print(matrix) 
        # # print(matrix[::-1])
        # return water

# # [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
# # [0, 0, 0, 1, 2, 2, 2, 1, 1, 2, 1, 0]
# # [0, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1]