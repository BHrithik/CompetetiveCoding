# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr:
            l = l+1
            curr = curr.next
        if l < k:
            return head
        curr = head
        prev = None
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        head.next = self.reverseKGroup(curr,k)
        return prev
        