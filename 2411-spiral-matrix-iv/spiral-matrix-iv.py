# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        left, top = 0, 0
        right, bottom = n, m
        while head:
            for i in range(left,right):
                if head:
                    matrix[top][i] = head.val
                    head = head.next
                else:
                    return matrix
            top += 1
            for i in range(top, bottom):
                if head:
                    matrix[i][right-1] = head.val
                    head = head.next
                else:
                    return matrix
            right -= 1
            for i in range(right-1,left-1, -1):
                if head:
                    matrix[bottom-1][i] = head.val
                    head = head.next
                else:
                    return matrix
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                if head:
                    matrix[i][left] = head.val
                    head = head.next
                else:
                    return matrix
            left += 1
        return matrix
