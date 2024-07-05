# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, cur, foll = head, head.next, head.next.next
        prev_critical_point = 0
        first_critical_point = 0
        index = 1
        max_dist = -1
        min_dist = float('inf')
        while foll:
            if prev.val < cur.val > foll.val or prev.val > cur.val < foll.val: # Current is critical
                if first_critical_point == 0:
                    first_critical_point = index
                else:
                    max_dist = index - first_critical_point
                    min_dist = min(min_dist,index - prev_critical_point)
                prev_critical_point = index
            index += 1
            prev = cur
            cur = foll
            foll = foll.next
        if min_dist == float('inf'):
            return [-1,max_dist]
        return [min_dist, max_dist]

                

