"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def helper(root):
            if not root:
                return None
            if root in oldToNew:
                return oldToNew[root]
            oldToNew[root] = Node(root.val)
            for nei in root.neighbors:
                oldToNew[root].neighbors.append(helper(nei))
            return oldToNew[root]
        return helper(node)

