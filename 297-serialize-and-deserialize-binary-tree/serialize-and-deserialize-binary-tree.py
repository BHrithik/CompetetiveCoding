# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        preOrder = []
        def dfs(root):
            if not root:
                preOrder.append('N')
                return
            preOrder.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(preOrder)

            
    def deserialize(self, data):
        values = data.split(',')
        self.i = 0
        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()