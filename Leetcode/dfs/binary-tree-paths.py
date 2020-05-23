# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        
    def dfs(self, root, data):
        if root.left is None and root.right is None:
            self.res.append("->".join(data))
        
        if root.left is not None:
            data.append(str(root.left.val))
            self.dfs(root.left, data)
            data.pop()
        
        if root.right is not None:
            data.append(str(root.right.val))
            self.dfs(root.right, data)
            data.pop()
        
        
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        data = [str(root.val)]
        self.dfs(root, data)
        return self.res