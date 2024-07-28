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
        slow = head
        fast = head.next
        while fast:
            nums.append(slow.val)
            slow = slow.next
            if not fast.next:
                break
            fast = fast.next.next
        maxSum = float('-inf')
        while slow:
            maxSum = max(maxSum,slow.val+nums.pop())
            slow = slow.next
        return maxSum