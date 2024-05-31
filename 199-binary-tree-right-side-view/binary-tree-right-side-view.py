# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        level = defaultdict(list)
        def bfs(root,l):
            if not root: return []
            level[l].append(root.val)
            l = l + 1
            if root.left:
                bfs(root.left,l)
            if root.right:
                bfs(root.right,l)
        bfs(root,0)
        print(level)
        ans = []
        for i in sorted(level.keys()):
            ans.append(level[i][-1])
        return ans