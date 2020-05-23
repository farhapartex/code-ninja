# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, value, sum_value):
        if root.left is None and root.right is None:
            return True if value == sum_value else False
        
        if root.left is not None:
            value += root.left.val
            #print("Left: ", value)
            if self.dfs(root.left, value, sum_value):
                return True
            else:
                value -= root.left.val
        
        if root.right is not None:
            value += root.right.val
            #print("Right: ", value)
            if self.dfs(root.right, value, sum_value):
                return True
            else:
                value -= root.right.val
        
        return False
            
            
    def hasPathSum(self, root: TreeNode, sum_value: int) -> bool:
        if root is None:
            return False
        return True if self.dfs(root, root.val, sum_value) else False
        
        
"""
Test cases:

[5,4,8,11,null,13,4,7,2,null,null,null,1]
22
[]
0
[]
2
[1]
1
[-3,null,-2]
-5
[-3,-2,-2]
-5
"""