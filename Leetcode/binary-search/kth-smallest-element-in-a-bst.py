# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        def inorder(node):
            if node:
                left = inorder(node.left)
                self.k -= 1
                if self.k == 0: return node.val
                right = inorder(node.right)
                return left if left is not None else right
        
        return inorder(root)
        