# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        queue, dist = [(root,1)], {}
        dist[root.val] = 0
        while queue:
            u = queue.pop(0)
            if u[0].left is None and u[0].right is None:
                return u[1]
            
            if u[0].left is not None:
                queue.append((u[0].left, u[1]+1))
            
            if u[0].right is not None:
                queue.append((u[0].right, u[1]+1))
        