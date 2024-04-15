# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = [0]
        if root == None: return
        def dfs(root,maxVal):
            if root == None: return
            if root.val >= maxVal:
                goodNodes[0] += 1
            maxVal = max(maxVal,root.val)
            dfs(root.left,maxVal)
            dfs(root.right,maxVal)
        dfs(root,float('-inf'))
        return goodNodes[0]