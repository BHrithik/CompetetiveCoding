# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = 0
        number2 = 0
        count = 1
        while l1:
            number1 += l1.val*count
            count = count*10
            l1 = l1.next
        count = 1
        while l2:
            number2 += l2.val *count
            count = count*10
            l2 = l2.next
        print(number1,number2)
        ans = number1+number2
        if ans==0:
            return ListNode(0)
        finalh = ListNode(-1)
        helper = finalh
        while ans:
            helper.next = ListNode(ans%10)
            ans = ans//10
            helper = helper.next
        return finalh.next