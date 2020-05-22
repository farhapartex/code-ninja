# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max = 0
        
        
    def dfs(self, node, root_val):
        if node is None:
            return 0
        
        left_value = self.dfs(node.left, node.val)
        right_value = self.dfs(node.right, node.val)
        
        self.max = max(self.max, (left_value+right_value))
        
        return max(left_value, right_value) + 1 if node.val == root_val else 0
    
        
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.dfs(root, root.val)
        return self.max
    
        