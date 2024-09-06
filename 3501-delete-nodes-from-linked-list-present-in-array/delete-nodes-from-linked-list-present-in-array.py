# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)  # Convert the list to a set for O(1) average-time complexity for lookups
        dummy = ListNode()  # Dummy node to simplify edge cases
        prev = dummy
        while head:
            if head.val not in nums:
                prev.next = head
                prev = prev.next
            head = head.next
        prev.next = None  # Ensure the last node points to None
        return dummy.next        