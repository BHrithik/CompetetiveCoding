class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(node, index):
            if not node or index >= len(arr):
                return False
            if node.val != arr[index]:
                return False
            if index == len(arr) - 1:
                return not node.left and not node.right
            return dfs(node.left, index + 1) or dfs(node.right, index + 1)
        
        return dfs(root, 0)
