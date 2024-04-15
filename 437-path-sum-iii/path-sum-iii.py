class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:    
        def updatePaths(root, sum):
            if root==None:return 0
            res = 0
            if root.val == sum:res += 1
            res += updatePaths(root.left, sum - root.val)
            res += updatePaths(root.right, sum - root.val)
            return res
        if root==None: return 0
        return self.pathSum(root.left,targetSum)+self.pathSum(root.right, targetSum)+updatePaths(root,targetSum)
