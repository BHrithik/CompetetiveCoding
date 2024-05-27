# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        num = set()
        def dfs(root,num):
            if not root:
                return None
            num.add(root.val)
            dfs(root.left,num)
            dfs(root.right,num)
        dfs(root,num)
        num = list(num)
        num.sort()
        print(num)
        if len(num) > 1:
            return num[1]
        else:
            return -1
        