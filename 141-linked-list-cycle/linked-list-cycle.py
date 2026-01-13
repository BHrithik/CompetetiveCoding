# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = head
        seen_nodes = set()
        while dummy:
            if dummy.next not in seen_nodes:
                seen_nodes.add(dummy.next)
                dummy = dummy.next
            else:
                return True
        return False