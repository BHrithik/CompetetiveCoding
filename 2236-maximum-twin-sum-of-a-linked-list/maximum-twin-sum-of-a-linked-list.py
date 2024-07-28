# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        new_head = head
        n = 0
        nums = []
        while new_head:
            n += 1
            nums.append(new_head.val)
            new_head = new_head.next
        return sorted([nums[i]+nums[n-1-i] for i in range(0,n//2)],reverse=True)[0]