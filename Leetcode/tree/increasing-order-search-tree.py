# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, last_node):
        if root.left is None and root.right is None:
            return (root, root)
        if root.left:
            main_root, last_node = self.inorder(root.left, last_node)
            root.left = None

            last_node.right = root
            #last_node.right = None
            last_node = last_node.right
        else:
            main_root, last_node = root, root
        
        if root.right:
            right_node, right_last = self.inorder(root.right, last_node)
            root.right = None
            last_node.right = right_node
            #print(right_node.val)
            last_node = right_last
        #print(main_root)
        return (main_root, last_node)
        
        
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return None if root is None else self.inorder(root, root)[0]
        