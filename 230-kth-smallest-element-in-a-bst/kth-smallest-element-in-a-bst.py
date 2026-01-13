# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n+= 1
            if n == k:
                return cur.val
            cur = cur.right
        # self.arr = []
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     self.arr.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return self.arr[k-1]