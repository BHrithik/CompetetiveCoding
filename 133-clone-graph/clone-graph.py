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
            new_node = Node(root.val)
            oldToNew[root] = new_node
            for nei in root.neighbors:
                oldToNew[root].neighbors.append(helper(nei))
            return new_node
        return helper(node)

