# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = defaultdict(int)
        levelC = 1
        def bfs(root,levelC):
            if not root:
                return
            level[levelC]= level[levelC] + root.val
            if root.left:
                bfs(root.left,levelC+1)
            if root.right:
                bfs(root.right,levelC+1)
        bfs(root,levelC)
        ans = [float('-inf'),-1]
        for i in level.keys():
            if ans[0] < level[i]:
                ans[0] = level[i]
                ans[1] = i
        return ans[1]
