# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, node, key):
        if node is None:
            return None
        
        if node.val == key:
            return node
        
        return self.search(node.right, key) if node.val < key else self.search(node.left, key)
        
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.search(root, val)
        