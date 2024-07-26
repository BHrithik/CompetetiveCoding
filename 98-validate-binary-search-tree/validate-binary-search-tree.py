# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def detect(root,left, right):
            if not root: return True
            if root.val > left and root.val < right:
                pass
            else:
                return False
            return detect(root.left,left,root.val) and detect(root.right,root.val,right)
        return detect(root,float('-inf'),float('inf'))
            