# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, value, L, R):
        if node is None:
            return value
        
        if node.val >= L and node.val <= R:
            #print(type(node.val))
            value += node.val
        
        value = self.dfs(node.left, value, L, R)
        value = self.dfs(node.right, value, L, R)
        
        return value
        
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.dfs(root, 0, L, R)
        