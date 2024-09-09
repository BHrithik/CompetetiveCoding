class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Count the total number of nodes in the list
        l = 0
        cur_node = head
        while cur_node:
            l += 1
            cur_node = cur_node.next
        baseNum = l // k
        extra = l % k
        arr = []
        cur_node = head
        for i in range(k):
            part_head = cur_node
            part_size = baseNum + (1 if extra > 0 else 0)
            extra -= 1
            for j in range(part_size - 1):
                if cur_node:
                    cur_node = cur_node.next
            if cur_node:
                next_part = cur_node.next
                cur_node.next = None
                cur_node = next_part
            arr.append(part_head)

        return arr
