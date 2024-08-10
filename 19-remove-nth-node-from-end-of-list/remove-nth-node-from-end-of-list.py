# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        new_head = head
        while new_head:
            new_head = new_head.next
            l += 1
        remove = l-n
        newHead = ListNode()
        newHead.next = head
        curHead = newHead
        for i in range(remove):
            curHead = curHead.next
        curHead.next = curHead.next.next
        return newHead.next