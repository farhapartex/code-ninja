# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_node = 0
        self.dist = {}
        
        
    def dfs(self, root):
        if root.left is None and root.right is None:
            self.max_node =  max(self.max_node, self.dist[root])
            return self.max_node
        
        if root.left is not None:
            self.dist[root.left] = self.dist[root] + 1
            self.dfs(root.left)
            
        if root.right is not None:
            self.dist[root.right] = self.dist[root] + 1
            self.dfs(root.right)
            
            
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.dist[root] = 0
        self.dfs(root)
        return self.max_node+1
        