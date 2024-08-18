class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getEdge(l,r,rightSide):
            res = -1
            while l <= r:
                m = (l+r)//2
                if nums[m] < target:
                    l = m+1
                elif nums[m] > target:
                    r = m-1
                else:
                    res = m
                    if rightSide:
                        l = m+1
                    else:
                        r = m-1
            return res
        l = 0
        r = len(nums)-1
        return [getEdge(l,r,False),getEdge(l,r,True)]

        
        