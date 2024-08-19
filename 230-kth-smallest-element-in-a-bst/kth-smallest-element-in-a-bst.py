# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            arr.append(root.val)
            traversal(root.right)
        traversal(root)
        return arr[k-1]
        # cur_root = root
        # stack = []
        # n = 0
        # while cur_root or stack:
        #     while cur_root:
        #         stack.append(cur_root)
        #         cur_root = cur_root.left
        #     # we get to the smallest element
        #     cur_root = stack.pop()
        #     n = n+1
        #     if n == k:
        #         return cur_root.val
        #     cur_root = cur_root.right
            
        # return -1