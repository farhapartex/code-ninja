# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, data, max_val):
        if node is None:
            return (data, max_val)
        data[node.val] = data.get(node.val, 0) + 1
        if data[node.val] > max_val:
            max_val = data[node.val]
        
        data, max_val = self.dfs(node.left, data, max_val)
        data, max_val = self.dfs(node.right, data, max_val)
        
        return (data, max_val)
        
        
    def findMode(self, root: TreeNode) -> List[int]:
        data, max_val = self.dfs(root, {}, -999999)
        return [d for d in data.keys() if data[d] == max_val]
        