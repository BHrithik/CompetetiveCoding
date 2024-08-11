# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeHash = set()
        while head:
            if head in nodeHash:
                return True
            nodeHash.add(head)
            head = head.next
        return False

