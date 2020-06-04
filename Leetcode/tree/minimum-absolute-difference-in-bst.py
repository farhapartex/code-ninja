# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def get_min_value(self, stack, value):
        min_value = 9999999
        for d in stack:
            min_value = min(abs(d-value), min_value)
        
        return min_value
    
    def min_service(self, stack, value, min_value):
        temp_min = self.get_min_value(stack, value)
        return min(min_value, temp_min)
        
        
    def dfs(self, node, stack, min_value):
        stack.append(node.val)
        
        if node.left is None and node.right is None:
            return (min_value, stack)
        
        
        if node.left is not None:
            min_value = self.min_service(stack, node.left.val, min_value)
            min_value, stack = self.dfs(node.left, stack, min_value)
            
        if node.right is not None:
            min_value = self.min_service(stack, node.right.val, min_value)
            min_value, stack = self.dfs(node.right, stack, min_value)
        
        return (min_value, stack)
        
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        
        min_val, stack = self.dfs(root, [], 999999)
        
        return min_val
        