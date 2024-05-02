class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        def dfs(node, index):
            # Check if the current node is null or index is out of bounds
            if not node or index >= len(arr):
                return False
            
            # Check if the current node's value doesn't match the current array value
            if node.val != arr[index]:
                return False
            
            # Check if this is the last node in the sequence and also a leaf node
            if index == len(arr) - 1:
                return not node.left and not node.right
            
            # Recursively check both left and right subtrees
            return dfs(node.left, index + 1) or dfs(node.right, index + 1)
        
        return dfs(root, 0)
