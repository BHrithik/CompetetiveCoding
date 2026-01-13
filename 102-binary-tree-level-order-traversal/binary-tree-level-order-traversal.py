# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.tree_dict= defaultdict(list)
        # def dfs(root, level):
        #     if not root:
        #         return
        #     self.tree_dict[level].append(root.val)
        #     dfs(root.left,level+1)
        #     dfs(root.right,level+1)
        # dfs(root,0)
        # return list(self.tree_dict.values())
        q = deque([root])
        count = 0
        res = []
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                res.append(level)
        return res