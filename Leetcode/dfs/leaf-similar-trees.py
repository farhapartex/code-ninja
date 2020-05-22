# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, data):
        if root.left is None and root.right is None:
            data.append(root.val)
            return data
        
        if root.left is not None:
            self.dfs(root.left, data)
        
        if root.right is not None:
            self.dfs(root.right, data)
        
        return data
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        data1, data2 = [], []
        if root1 is None and root2 is None:
            return True
        data1 = self.dfs(root1, data1)
        data2 = self.dfs(root2, data2)
        #print(data1, " ", data2)
        return True if data1 == data2 else False
        