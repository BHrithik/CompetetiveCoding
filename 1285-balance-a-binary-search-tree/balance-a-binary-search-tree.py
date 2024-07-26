# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr =[]
        def populateArr(root):
            if not root: return
            populateArr(root.left)
            arr.append(root.val)
            populateArr(root.right)
        populateArr(root)
        arr.sort()
        def populateTree(nums):
            if not nums:
                return
            n = len(nums)//2
            mid = TreeNode(nums[n])
            mid.left = populateTree(nums[0:n])
            mid.right = populateTree(nums[n+1:])
            return mid
        ans = populateTree(arr)
        return ans
