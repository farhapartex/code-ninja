# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, min_node, second_min):
        if node is None:
            return (min_node, second_min)
        
        if node.val < min_node:
            min_node = node.val
        
        if node.val > min_node and node.val < second_min:
            second_min = node.val
        
        min_node, second_min = self.dfs(node.left, min_node, second_min)
        
        min_node, second_min = self.dfs(node.right, min_node, second_min)
        #print("min_node ",min_node)
        return (min_node, second_min)
    
    
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min_node, second_min = self.dfs(root, 9999999999, 99999999999)
        
        return -1 if second_min==99999999999 else second_min
        