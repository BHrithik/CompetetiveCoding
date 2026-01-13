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
            if dummy not in seen_nodes:
                seen_nodes.add(dummy)
            else:
                return True
            dummy = dummy.next
        return False