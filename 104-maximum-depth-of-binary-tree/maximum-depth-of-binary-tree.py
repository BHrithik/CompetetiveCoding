# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root,cur_depth):
            nonlocal res
            if not root:
                res = max(res,cur_depth)
                return
            helper(root.left,cur_depth+1)
            helper(root.right,cur_depth+1)
        helper(root,0)
        return res
