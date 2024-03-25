# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        
        adjDict = defaultdict(list)
        q = deque([root])

        while q:
            node = q.popleft()
            if node.left:
                adjDict[node].append(node.left)
                adjDict[node.left].append(node)

                q.append(node.left)
            if node.right:
                adjDict[node].append(node.right)
                adjDict[node.right].append(node)

                q.append(node.right)

        visit = set()
        res = []
        q = deque([(target,0)])
        visit.add(target)
        while q:
            node, dist = q.popleft()
            if dist == k:
                res.append(node.val)
            else:
                for i in adjDict[node]:
                    if i not in visit:
                        visit.add(i)
                        q.append((i,dist+1))
        return res
            
            
        
        