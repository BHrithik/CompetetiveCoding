# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def helper(root,res):
            if not root:
                return 0
            left = helper(root.left,res)
            right = helper(root.right,res)
            res[0] = max(res[0],left+right)
            return 1+max(left,right)
        helper(root,res)
        return res[0]