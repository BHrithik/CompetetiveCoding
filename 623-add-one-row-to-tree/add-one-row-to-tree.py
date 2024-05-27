# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def add(root, val, depth, cur_depth):
            if depth == 1:
                new_root = TreeNode(val)
                new_root.left = root
                return new_root
            if not root:
                return None
            if cur_depth == depth-1:
                root.left = TreeNode(val,root.left,None)
                root.right = TreeNode(val,None,root.right)
                return root
            root.left = add(root.left,val,depth,cur_depth+1)
            root.right = add(root.right,val,depth,cur_depth+1)
            return root
        return add(root,val,depth,1)