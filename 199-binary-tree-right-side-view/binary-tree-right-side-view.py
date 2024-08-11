# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dictNew = defaultdict(list)
        level = 0
        def helper(root,level):
            if not root: return
            helper(root.left,level+1)
            dictNew[level].append(root.val)
            helper(root.right,level+1)
        helper(root,0)
        print(dictNew.values())
        return [dictNew[i][-1] for i in sorted(dictNew.keys())]