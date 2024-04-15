# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_length = 0

        def dfs(node, prevDir, length):
            nonlocal max_length
            if not node:
                return
            # Update maximum zigzag length found so far
            max_length = max(max_length, length)

            # Explore both possible directions from current node
            if prevDir == "left":
                # We came to this node from a left move, check the right child
                if node.right:
                    dfs(node.right, 'right', length + 1)
                # Additionally, explore left child starting new count
                if node.left:
                    dfs(node.left, 'left', 1)
            elif prevDir == "right":
                # We came to this node from a right move, check the left child
                if node.left:
                    dfs(node.left, 'left', length + 1)
                # Additionally, explore right child starting new count
                if node.right:
                    dfs(node.right, 'right', 1)
            else:
                # First call for the root, consider both children
                if node.left:
                    dfs(node.left, 'left', 1)
                if node.right:
                    dfs(node.right, 'right', 1)

        # Initial call from the root
        dfs(root, None, 0)
        return max_length

# Example to use the class and method
# Assuming some binary tree `root` is defined elsewhere and passed here
# sol = Solution()
# max_zigzag_length = sol.longestZigZag(root)
