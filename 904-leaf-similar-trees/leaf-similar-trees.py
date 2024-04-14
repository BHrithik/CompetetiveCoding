# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(root,leaf):
            if not root:
                return
            if not root.right and not root.left:
                leaf.append(root.val)
            getLeaves(root.left,leaf)
            getLeaves(root.right,leaf)
        leaf1, leaf2 = [],[]
        getLeaves(root1,leaf1)
        getLeaves(root2,leaf2)
        return leaf1==leaf2