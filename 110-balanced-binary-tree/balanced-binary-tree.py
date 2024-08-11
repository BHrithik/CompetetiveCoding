# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ischk = True
        def helper(root):
            if not root:
                return 0
            left  = helper(root.left)
            right = helper(root.right)
            if left is None or right is None:
                return None
            if left-right > 1 or left-right < -1:
                self.ischk = False
            else:
                return max(left,right)+1
        helper(root)
        return self.ischk
