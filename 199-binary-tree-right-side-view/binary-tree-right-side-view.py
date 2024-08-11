# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        res = []
        dotha = deque([root])
        while dotha:
            cur_size = len(dotha)
            for i in range(cur_size):
                cur_root = dotha.popleft()
                if cur_root.left: dotha.append(cur_root.left)
                if cur_root.right: dotha.append(cur_root.right)
            res.append(cur_root.val)
        return res