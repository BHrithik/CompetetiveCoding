# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def helper(root):
            nonlocal maxSum
            if not root:
                return 0
            left = max(helper(root.left),0)
            right = max(helper(root.right),0)
            maxSum = max(maxSum, left+right+root.val)
            return root.val+max(left,right)
        helper(root)
        return maxSum