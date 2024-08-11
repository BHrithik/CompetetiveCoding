# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        treeDict = defaultdict(list)
        level = 0 # 0 is root
        def helper(root,level):
            if not root: return
            helper(root.left,level+1)
            treeDict[level].append(root.val)
            helper(root.right,level+1)
        helper(root,level)
        res = []
        for key in sorted(treeDict.keys()):
            res.append(treeDict[key])
        return res