"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        nodeMap = {}
        cur = head
        while cur:
            nodeMap[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            nodeMap[cur].next = nodeMap.get(cur.next)
            nodeMap[cur].random = nodeMap.get(cur.random)
            cur = cur.next
        return nodeMap[head]


