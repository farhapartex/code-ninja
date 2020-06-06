# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_left_node(self, node):
        try:
            return node.left
        except:
            return None
    
    def get_right_node(self, node):
        try:
            return node.right
        except:
            return None
        
    def tree_traverse(self, node1, node2):
        if node1 is None and node2 is None:
            return None
        
        new_node = TreeNode()
        
        if node1 is None and node2 is not None:
            new_node.val = node2.val
        elif node1 is not None and node2 is None:
            new_node.val = node1.val
        else:
            new_node.val = node1.val + node2.val
        
        
        node1_left = self.get_left_node(node1)
        node2_left = self.get_left_node(node2)
        
        node1_right = self.get_right_node(node1)
        node2_right = self.get_right_node(node2)
        
        new_node.left = self.tree_traverse(node1_left, node2_left)
        new_node.right = self.tree_traverse(node1_right, node2_right)
        
        return new_node
        
        
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        new_tree = self.tree_traverse(t1, t2)
        
        #print(new_tree)
        
        return new_tree
    

    # def mergeTrees2(self, t1, t2):
    # 	if t1 and t2:
    #         t3 = TreeNode(t1.val + t2.val) 
    #         t3.left = self.mergeTrees(t1.left, t2.left)
    #         t3.right = self.mergeTrees(t1.right, t2.right)
    #         return t3
    #     elif t1:
    #         return t1
    #     elif t2:
    #         return t2
        