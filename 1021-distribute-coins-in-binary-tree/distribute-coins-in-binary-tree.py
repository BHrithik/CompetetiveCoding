# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def dfs(root):
            if not root:
                return 0
            left_excess = dfs(root.left)
            right_excess = dfs(root.right)
            self.moves+=abs(left_excess)+abs(right_excess)
            return root.val + left_excess + right_excess -1
        dfs(root)
        return self.moves
            