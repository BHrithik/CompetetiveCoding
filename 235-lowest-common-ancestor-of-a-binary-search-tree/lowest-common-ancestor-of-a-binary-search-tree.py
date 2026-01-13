# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
            return root
        if (root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)
        
        # cur = root
        # while cur:
        #     if p.val > cur.val and q.val > cur.val:
        #         cur = cur.right
        #     elif p.val < cur.val and q.val < cur.val:
        #         cur = cur.left
        #     else:
        #         return cur