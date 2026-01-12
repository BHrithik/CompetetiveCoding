# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_pointer = head
        prev = None
        while cur_pointer:
            nxt = cur_pointer.next
            cur_pointer.next = prev
            prev = cur_pointer
            cur_pointer = nxt
        return prev
