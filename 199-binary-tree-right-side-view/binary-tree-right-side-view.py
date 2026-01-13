# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        tree_dict = defaultdict(list)
        def dfs(root, level):
            if not root:
                return
            dfs(root.left,level+1)
            tree_dict[level].append(root.val)
            dfs(root.right,level+1)
        dfs(root, 0)
        res = []
        for i in range(0,len(tree_dict)):
            res.append(tree_dict[i][-1])
        return res