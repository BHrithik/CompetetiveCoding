# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = root
        dummy = self.tree
        self.arr = []
        def dfs(dummy):
            if not dummy:
                return
            self.arr.append(dummy.val)
            if dummy.left:
                dfs(dummy.left)
            if dummy.right:
                dfs(dummy.right)
        dfs(dummy)
        print(self.arr)
        self.arr.sort()
        self.count = 0


    def next(self) -> int:
        self.count += 1
        return self.arr[self.count-1]

    def hasNext(self) -> bool:
        return self.count < len(self.arr)
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()