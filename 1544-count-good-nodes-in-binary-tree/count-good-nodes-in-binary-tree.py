# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def helper(root,rootVal):
            if not root: return
            if root.val >= rootVal:
                print(f"Value {root.val} is greater than {rootVal}")
                self.count += 1
            helper(root.left,max(rootVal,root.val))
            helper(root.right,max(rootVal,root.val))
        helper(root,float('-inf'))
        return self.count