class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        q = deque()
        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if left > q[0]:
                q.popleft()
            if i >= k -1:
                left = left+1
                res.append(nums[q[0]])
        return res
            
