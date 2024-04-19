class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack=[]
        nums1 = [float('-inf')] + nums + [float('-inf')]
        total1=0
        for i in range(len(nums1)):
            while stack and nums1[stack[-1]]>nums1[i]:
                cur=stack.pop()
                total1+=nums1[cur]*(i-cur)*(cur-stack[-1])
            stack.append(i)
        nums = [float('inf')] + nums + [float('inf')]
        stack = []
        total = 0
        print(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                cur = stack.pop()
                total += nums[cur]*(i-cur)*(cur-stack[-1])
            stack.append(i)
        return total-total1