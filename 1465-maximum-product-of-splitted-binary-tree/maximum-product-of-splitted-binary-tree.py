# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def traverse(root):
            if not root:return 0
            if root in memo:
                return memo[root]
            else:
                memo[root] = root.val+traverse(root.left)+traverse(root.right)
            return memo[root]
        self.ts = traverse(root)
        self.ans = 0
        def findMaxProduct(root):
            if not root: return
            x = memo[root]
            self.ans = max(self.ans,(self.ts-x)*x)
            findMaxProduct(root.left)
            findMaxProduct(root.right)
        findMaxProduct(root)
        return self.ans%(10**9+7)