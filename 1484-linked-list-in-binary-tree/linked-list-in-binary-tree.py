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
        d = deque([root])

        def dfs(node, root):
            if not node:  # Reached the end of the list, successful match
                return True
            if not root or root.val != node.val:  # Mismatch between current tree node and list node or Reached the end of the tree, but still nodes in the list
                return False
            # Try both left and right children
            return dfs(node.next, root.left) or dfs(node.next, root.right)

        while d:
            for i in range(len(d)):
                cur_root = d.popleft()
                if cur_root.val == current_node.val and dfs(current_node, cur_root):
                    return True
                if cur_root.left:
                    d.append(cur_root.left)
                if cur_root.right:
                    d.append(cur_root.right)
        return False

        