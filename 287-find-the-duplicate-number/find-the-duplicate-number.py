class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # First observation since nums is of size n and values can be from [1,n]
        # We should look at them like a linked list where each value in the array is 
        # pointer to the next one
        slow, fast = 0, 0 # We know that the first element is not the duplicate as there is no 0, The elements start at 1
        while True: # Find the first point of intersection with fast and slow pointers.
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0 # Start a new slow pointer from the beginning 
        # and according to Floyd's algorithm it should reach the point of intersection at the same time as fast
        while True:
            fast = nums[fast]
            slow2 = nums[slow2]
            if fast == slow2:
                return fast