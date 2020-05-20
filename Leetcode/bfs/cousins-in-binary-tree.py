# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue, dist, parent = [root], {}, {}
        dist[root.val] = 0
        parent[root.val] = None
        x_dist, y_dist, x_parent, y_parent  = 0, 0, 0, 0
        
        while queue:
            u = queue.pop(0)
            if u.val == x:
                x_dist = dist[x]
                x_parent = parent[x]
            
            elif u.val == y:
                y_dist = dist[y]
                y_parent = parent[y]
                
            if u.left is not None:
                dist[u.left.val]  = dist[u.val] + 1
                queue.append(u.left)
                parent[u.left.val] = u.val
                    
            
            if u.right is not None:
                dist[u.right.val]  = dist[u.val] + 1
                queue.append(u.right)
                parent[u.right.val] = u.val
                
        
        return True if x_dist == y_dist and x_parent != y_parent else False
            
        
        