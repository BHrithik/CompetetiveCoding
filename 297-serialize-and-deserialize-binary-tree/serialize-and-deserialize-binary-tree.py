# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if not root: return "N,"
            return str(root.val)+","+dfs(root.left)+dfs(root.right)
        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # return
        values = iter(data.split(","))
        def helper(values):
            val = next(values)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = helper(values)
            node.right = helper(values)
            return node
        return helper(values)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))