# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, prevValue):
            if not root:
                return
            if root.val >= prevValue:
                self.count += 1
            dfs(root.left,max(root.val,prevValue))
            dfs(root.right,max(root.val,prevValue))
        dfs(root,float('-inf'))
        return self.count