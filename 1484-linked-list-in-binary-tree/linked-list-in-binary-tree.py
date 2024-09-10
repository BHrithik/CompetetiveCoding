# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, current_node: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        potential_starts = []
        def traversal(root):
            if not root:
                return
            if root.val == current_node.val:
                potential_starts.append(root)
            traversal(root.left)
            traversal(root.right)

        def dfs(node, root):
            if not node:  # Reached the end of the list, successful match
                return True
            if not root:  # Reached the end of the tree, but still nodes in the list
                return False
            if root.val != node.val:  # Mismatch between current tree node and list node
                return False
            # Try both left and right children
            return dfs(node.next, root.left) or dfs(node.next, root.right)

        traversal(root)
        for pt_start in potential_starts:
            if dfs(current_node, pt_start):
                return True
        return False

        