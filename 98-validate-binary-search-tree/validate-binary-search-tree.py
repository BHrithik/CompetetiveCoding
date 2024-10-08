# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,minVal,maxVal):
            if not root: return True
            if not minVal < root.val < maxVal:
                return False
            return helper(root.left,minVal,root.val) and helper(root.right,root.val,maxVal)
        return helper(root,float('-inf'),float('inf'))

