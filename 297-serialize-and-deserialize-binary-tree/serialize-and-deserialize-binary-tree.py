# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        preOrder = []
        def helper(root):
            if not root:
                preOrder.append("None")
                return
            preOrder.append(str(root.val))
            helper(root.left)
            helper(root.right)
        helper(root)
        return ",".join(preOrder)

    def deserialize(self, data):
        vals = data.split(',')
        self.i = 0
        def helper():
            if vals[self.i] == "None":
                self.i += 1
                return None
            new_node = TreeNode(int(vals[self.i]))
            self.i += 1
            new_node.left  = helper()
            new_node.right = helper()
            return new_node
        return helper()