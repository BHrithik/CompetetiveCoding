# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        tree_arr = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            tree_arr.append(root.val)
            dfs(root.right)
        print(tree_arr)
        temp_root = root
        dfs(temp_root)
        def rep_nodes(root):
            if not root: return
            cur_sum = sum(i for i in tree_arr if i > root.val)
            cur_sum += root.val
            rep_nodes(root.left)
            root.val = cur_sum
            rep_nodes(root.right)
        rep_nodes(root)
        return root
