# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree = defaultdict(list)
        children = []
        for (p,c,il) in descriptions:
            tree[p].append((c,il))
            children.append(c)
        print(tree)
        print(children)
        for i in tree:
            if i not in children:
                root = i
        def dfs(root):
            if not tree[root]: return TreeNode(root)
            ans = TreeNode(root)
            for i in tree[root]:
                if i[1] == 1: #Left Node
                    ans.left = dfs(i[0])
                if i[1] == 0: #Right Node
                    ans.right = dfs(i[0])
            return ans
        res = dfs(root)
        return res